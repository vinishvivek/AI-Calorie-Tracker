from __future__ import annotations

class NutritionPrompts:
    FOOD_IDENTIFICATION_PROMPT = """
Context: Understand the food item in the image.
Instruction: Analyse the contents and approximate the weight of the items provided.
Image: [Image attached]
Output: Provide a list of items you see along with their approximate weight based on the image.
""".strip()

    NUTRITION_INFORMATION_PROMPT = """
    Analyze the food image and return ONLY valid JSON.

    Rules:
    - No markdown
    - No explanations
    - No triple backticks
    - Use double quotes
    - All numeric values must be integers
    - Include only visible food items

    Return exactly:
    {
      "items": [
        {
          "name": "string",
          "portion": "string",
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