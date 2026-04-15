from __future__ import annotations

import gradio as gr
import pandas as pd

from services.nutrition_estimation_service import NutritionEstimationService
from utils.file_utils import FileUtils


class CalorieTrackerApp:
    """Build and manage the Gradio interface for the AI Calorie Tracker."""

    def __init__(self) -> None:
        """Initialize the application with the nutrition analysis service."""
        self._nutrition_service = NutritionEstimationService()

    def analyze_image(self, image_path: str) -> tuple[str, str, pd.DataFrame]:
        """Analyze an uploaded food image and return detected items, summary, and nutrition table."""
        try:
            if not image_path:
                raise gr.Error("Please upload an image.")

            FileUtils.validate_image_path(image_path)

            identified_foods, nutrition_result = (
                self._nutrition_service.run_full_analysis(image_path=image_path)
            )

            dataframe = pd.DataFrame(nutrition_result.to_table_rows())

            return (
                identified_foods,
                nutrition_result.summary_text(),
                dataframe,
            )

        except Exception as exc:
            raise gr.Error(f"Analysis failed: {str(exc)}")

    def build_interface(self) -> gr.Blocks:
        """Create and return the Gradio interface for the calorie tracking application."""
        with gr.Blocks() as interface:
            gr.Markdown("# 🍳 AI Calorie Tracker")
            gr.Markdown(
                "Upload a food image to identify items and estimate calories 🔥 "
            )

            with gr.Row():
                with gr.Column(scale=1):
                    image_input = gr.Image(
                        type="filepath", label="Upload Food Image", height=300
                    )
                    analyze_button = gr.Button("Analyze")

                with gr.Column(scale=2):
                    summary_output = gr.Textbox(
                        label="Etimated Nutrition",
                        lines=6,
                    )
                    identified_foods_output = gr.Markdown(
                        label="Detected Ingredients & Portions",
                    )
                    table_output = gr.Dataframe(label="Detailed Nutrition Breakdown")

            analyze_button.click(
                fn=self.analyze_image,
                inputs=image_input,
                outputs=[
                    identified_foods_output,
                    summary_output,
                    table_output,
                ],
            )

        return interface
