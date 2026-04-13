from __future__ import annotations

class NutritionPrompts:
    FOOD_IDENTIFICATION_PROMPT = """
Context: Understand the food item in the image.
Instruction: Analyse the contents and approximate the weight of the items provided.
Image: [Image attached]
Output: Provide a list of items you see along with their approximate weight based on the image.
""".strip()

    NUTRITION_INFORMATION_PROMPT = """
You are a strict JSON-only nutrition analysis engine.

Analyze the provided image and identify all visible food items.

For each food item:
- name: standardized food name
- portion: estimated portion (e.g., "1 bowl", "200g", "1 slice")
- calories: estimated kcal for that portion (integer)
- protein_g: grams of protein (integer)
- carbs_g: grams of carbohydrates (integer)
- fat_g: grams of fat (integer)
- fiber_g: grams of fiber (integer, if applicable, else 0)
- sugar_g: grams of sugar (integer, if applicable, else 0)

Constraints:
- Output MUST be valid JSON only (no markdown, no explanations)
- Do NOT include any text outside the JSON
- Use realistic nutritional estimates based on standard nutrition references
- If uncertain, provide best reasonable estimate
- Do not include non-food items
- All numeric values must be integers

Return exactly this schema:
{
  "items": [
    {
      "name": "",
      "portion": "",
      "calories": 0,
      "protein_g": 0,
      "carbs_g": 0,
      "fat_g": 0,
      "fiber_g": 0,
      "sugar_g": 0
    }
  ],
  "total": {
    "calories": 0,
    "protein_g": 0,
    "carbs_g": 0,
    "fat_g": 0,
    "fiber_g": 0,
    "sugar_g": 0
  }
}
""".strip()