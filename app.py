from __future__ import annotations

import gradio as gr
import pandas as pd

from services.nutrition_estimation_service import NutritionEstimationService
from utils.file_utils import FileUtils


class CalorieTrackerApp:
    def __init__(self) -> None:
        self._nutrition_service = NutritionEstimationService()

    def analyze_image(self, image_path: str) -> tuple[str, str, pd.DataFrame]:
        try:
            if not image_path:
                raise gr.Error("Please upload an image.")

            FileUtils.validate_image_path(image_path)

            identified_foods, nutrition_result = self._nutrition_service.run_full_analysis(
                image_path=image_path
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
        with gr.Blocks() as interface:
            gr.Markdown("# AI Calorie Tracker")
            gr.Markdown("Upload a food image to identify items and estimate calories.")

            image_input = gr.Image(type="filepath", label="Upload Food Image")
            analyze_button = gr.Button("Analyze")

            identified_foods_output = gr.Textbox(
                label="Identified Food Items",
                lines=8,
            )
            summary_output = gr.Textbox(
                label="Nutrition Summary",
                lines=8,
            )
            table_output = gr.Dataframe(label="Nutrition Breakdown")

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


if __name__ == "__main__":
    app = CalorieTrackerApp()
    interface = app.build_interface()
    interface.launch()