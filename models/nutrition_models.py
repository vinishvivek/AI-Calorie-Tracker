from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Any

@dataclass
class FoodItem:
    name: str
    portion: str
    calories: int
    protein_g: int
    carbs_g: int
    fat_g: int
    fiber_g: int
    sugar_g: int

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

@dataclass
class NutritionTotal:
    calories: int
    protein_g: int
    carbs_g: int
    fat_g: int
    fiber_g: int
    sugar_g: int

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

@dataclass
class NutritionResult:
    items: list[FoodItem]
    total: NutritionTotal

    def to_table_rows(self) -> list[dict[str, Any]]:
        return [item.to_dict() for item in self.items]

    def summary_text(self) -> str:
        return (
            "----------------------------------------------\n"
            f"Total Calories:   |{self.total.calories} kcal\n"
            f"Protein:          |{self.total.protein_g} g\n"
            f"Carbs:            |{self.total.carbs_g} g\n"
            f"Fat:              |{self.total.fat_g} g\n"
            f"Fiber:            |{self.total.fiber_g} g\n"
            f"Sugar:            |{self.total.sugar_g} g\n"
            "----------------------------------------------\n"
        )