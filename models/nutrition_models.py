from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Any

@dataclass
class FoodItem:
    name: str
    portion: str
    calories: int
    proteins_g: int
    carbs_g: int
    fats_g: int
    fiber_g: int
    sugar_g: int

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

@dataclass
class NutritionTotal:
    pass

@dataclass
class NutritionResult:
    pass