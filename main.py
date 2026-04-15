from __future__ import annotations

from app import CalorieTrackerApp


class ApplicationRunner:
    def __init__(self) -> None:
        self._app = CalorieTrackerApp()

    def run(self) -> None:
        interface = self._app.build_interface()
        interface.launch()


def main() -> None:
    runner = ApplicationRunner()
    runner.run()


if __name__ == "__main__":
    main()