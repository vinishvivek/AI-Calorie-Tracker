from __future__ import annotations

from app import CalorieTrackerApp


class ApplicationRunner:
    """Launch the calorie tracker application through a dedicated entry-point runner."""

    def __init__(self) -> None:
        """Initialize the application runner with the Gradio app wrapper."""
        self._app = CalorieTrackerApp()

    def run(self) -> None:
        """Build and launch the Gradio interface."""
        interface = self._app.build_interface()
        interface.launch()


def main() -> None:
    """Application entry point for local execution."""
    runner = ApplicationRunner()
    runner.run()


if __name__ == "__main__":
    main()
