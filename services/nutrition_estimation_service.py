from __future__ import annotations

import json
import re

from models.nutrition_models import FoodItem, NutritionResult, NutritionTotal
from prompts.nutrition_prompts import NutritionPrompts
from services.vision_service import VisionService


class NutritionEstimationService:
    """Coordinate food identification, nutrition estimation, and response parsing for food images."""

    def __init__(self) -> None:
        """Initialize the service with the vision analysis dependency."""
        self._vision_service = VisionService()

    def identify_foods(self, image_path: str) -> str:
        """Identify visible food items and approximate portions from an input image."""
        return self._vision_service.query_image(
            image_to_llm=image_path,
            prompt=NutritionPrompts.FOOD_IDENTIFICATION_PROMPT,
        )

    def estimate_nutrition(self, image_path: str) -> NutritionResult:
        """Estimate nutrition values for the detected food in an input image."""
        raw_response = self._vision_service.query_image(
            image_to_llm=image_path,
            prompt=NutritionPrompts.NUTRITION_INFORMATION_PROMPT,
        )

        parsed_response = self._parse_llm_json_response(raw_response)

        items = [
            FoodItem(
                name=item["name"],
                portion=item["portion"],
                calories=int(item["calories"]),
                protein_g=int(item["protein_g"]),
                carbs_g=int(item["carbs_g"]),
                fat_g=int(item["fat_g"]),
                fiber_g=int(item["fiber_g"]),
                sugar_g=int(item["sugar_g"]),
            )
            for item in parsed_response["items"]
        ]

        total = parsed_response["total"]
        nutrition_total = NutritionTotal(
            calories=int(total["calories"]),
            protein_g=int(total["protein_g"]),
            carbs_g=int(total["carbs_g"]),
            fat_g=int(total["fat_g"]),
            fiber_g=int(total["fiber_g"]),
            sugar_g=int(total["sugar_g"]),
        )

        return NutritionResult(items=items, total=nutrition_total)

    def run_full_analysis(self, image_path: str) -> tuple[str, NutritionResult]:
        """Run the complete analysis pipeline for a food image."""
        identified_foods = self.identify_foods(image_path)
        nutrition_result = self.estimate_nutrition(image_path)
        return identified_foods, nutrition_result

    def _parse_llm_json_response(self, raw_response: str) -> dict:
        """Clean, extract, and parse JSON-like model output into a Python dictionary."""
        cleaned_response = raw_response.strip()

        cleaned_response = re.sub(r"^```json\s*", "", cleaned_response, flags=re.IGNORECASE)
        cleaned_response = re.sub(r"^```\s*", "", cleaned_response)
        cleaned_response = re.sub(r"\s*```$", "", cleaned_response)

        if not cleaned_response.endswith("}") and not cleaned_response.endswith("]}"):
            raise ValueError(
                "The model response appears to be truncated before the JSON finished. "
                "Try increasing max_tokens."
            )

        json_match = re.search(r"\{.*\}", cleaned_response, re.DOTALL)
        if not json_match:
            raise ValueError(
                f"Could not find valid JSON object in model response:\n{raw_response}"
            )

        json_string = json_match.group(0)
        json_string = re.sub(r",(\s*[}\]])", r"\1", json_string)

        try:
            return json.loads(json_string)
        except json.JSONDecodeError as exc:
            raise ValueError(
                f"Failed to parse model JSON response.\nRaw response was:\n{raw_response}"
            ) from exc