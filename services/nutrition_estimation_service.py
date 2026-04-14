from __future__ import annotations

import json

from models.nutrition_models import FoodItem, NutritionResult, NutritionTotal
from prompts.nutrition_prompts import NutritionPrompts
from services.vision_service import VisionService


class NutritionEstimationService:
    def __init__(self) -> None:
        self._vision_service = VisionService()

    def identify_foods(self, image_path: str) -> str:
        return self._vision_service.query_image(
            image_to_llm=image_path,
            prompt=NutritionPrompts.FOOD_IDENTIFICATION_PROMPT,
            max_tokens=250,
        )

    def estimate_nutrition(self, image_path: str) -> NutritionResult:
        raw_response = self._vision_service.query_image(
            image_to_llm=image_path,
            prompt=NutritionPrompts.NUTRITION_INFORMATION_PROMPT,
            max_tokens=400,
        )

        parsed_response = json.loads(raw_response)

        items = [
            FoodItem(
                name=item["name"],
                portion=item["portion"],
                calories=item["calories"],
                protein_g=item["protein_g"],
                carbs_g=item["carbs_g"],
                fat_g=item["fat_g"],
                fiber_g=item["fiber_g"],
                sugar_g=item["sugar_g"],
            )
            for item in parsed_response["items"]
        ]

        total = parsed_response["total"]
        nutrition_total = NutritionTotal(
            calories=total["calories"],
            protein_g=total["protein_g"],
            carbs_g=total["carbs_g"],
            fat_g=total["fat_g"],
            fiber_g=total["fiber_g"],
            sugar_g=total["sugar_g"],
        )

        return NutritionResult(items=items, total=nutrition_total)

    def run_full_analysis(self, image_path: str) -> tuple[str, NutritionResult]:
        identified_foods = self.identify_foods(image_path)
        nutrition_result = self.estimate_nutrition(image_path)
        return identified_foods, nutrition_result