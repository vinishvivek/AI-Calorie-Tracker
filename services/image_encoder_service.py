from __future__ import annotations

import base64
import os
import io
from pathlib import Path

from PIL import Image

class ImageEncoderService:
    """Handle image loading and base64 encoding for model-ready image input."""

    @staticmethod
    def encode_image_to_base64(image_source: str | Image.Image) -> str:
        """Convert an image file path or PIL image into a base64-encoded string."""
        if isinstance(image_source, str):
            if not os.path.exists(image_source):
                raise FileNotFoundError(f"Image not found: {image_source}")

            with open(image_source, "rb") as image_file:
                return base64.b64encode(image_file.read()).decode("utf-8")

        if isinstance(image_source, Image.Image):
            buffered = io.BytesIO()
            image_format = image_source.format or "JPEG"
            image_source.save(buffered, format=image_format)
            return base64.b64encode(buffered.getvalue()).decode("utf-8")

        raise TypeError("image_source must be File Path or PIL Image Object")

    @staticmethod
    def get_mime_type(image_path: str) -> str:
        """Return the MIME type for a supported image file based on its extension."""
        extension = Path(image_path).suffix.lower()

        mapping = {
            ".png": "image/png",
            ".jpg": "image/jpeg",
            ".jpeg": "image/jpeg",
            ".webp": "image/webp",
        }

        return mapping.get(extension, "image/jpeg")