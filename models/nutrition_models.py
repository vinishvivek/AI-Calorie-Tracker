from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Any

@dataclass
class FoodItem:
    """Represent a single detected food item and its estimated nutrition values."""
    name: str
    portion: str
    calories: int
    protein_g: int
    carbs_g: int
    fat_g: int
    fiber_g: int
    sugar_g: int

    def to_dict(self) -> dict[str, Any]:
        """Convert the food item into a dictionary for tabular display or serialization."""
        return asdict(self)

@dataclass
class NutritionTotal:
    """Represent the aggregated nutrition totals for a full meal or image."""
    calories: int
    protein_g: int
    carbs_g: int
    fat_g: int
    fiber_g: int
    sugar_g: int

    def to_dict(self) -> dict[str, Any]:
        """Convert the nutrition totals into a dictionary representation."""
        return asdict(self)

@dataclass
class NutritionResult:
    """Store the complete nutrition analysis result, including individual items and totals."""
    items: list[FoodItem]
    total: NutritionTotal

    def to_table_rows(self) -> list[dict[str, Any]]:
        """Convert food items into row dictionaries suitable for DataFrame rendering."""
        return [item.to_dict() for item in self.items]

    def summary_text(self) -> str:
        """Generate a readable summary of the total nutrition values."""
        return (
            f"Total Calories:{self.total.calories} kcal\n"
            f"Protein: {self.total.protein_g} g\n"
            f"Carbs: {self.total.carbs_g} g\n"
            f"Fat: {self.total.fat_g} g\n"
            f"Fiber:{self.total.fiber_g} g\n"
            f"Sugar: {self.total.sugar_g} g\n"
            "⚠ ️Estimates are approximate and based on visual analysis"
        )