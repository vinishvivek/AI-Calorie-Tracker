from __future__ import annotations

from pathlib import Path


class FileUtils:
    ALLOWED_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp"}

    @classmethod
    def validate_image_path(cls, image_path: str) -> None:
        path = Path(image_path)

        if not path.exists():
            raise FileNotFoundError(f"Image file does not exist: {image_path}")

        if path.suffix.lower() not in cls.ALLOWED_EXTENSIONS:
            raise ValueError(
                f"Unsupported image format: {path.suffix}. "
                f"Allowed formats: {', '.join(sorted(cls.ALLOWED_EXTENSIONS))}"
            )