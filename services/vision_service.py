from __future__ import annotations

from PIL import Image

from clients.openai_client import OpenAIClientFactory
from config.settings import settings
from services.image_encoder_service import ImageEncoderService

class VisionService:
    def __init__(self) -> None:
        self._client = OpenAIClientFactory.create()

    def query_image(
        self,
        image_to_llm: str | Image.Image,
        prompt: str,
        ) -> str:
        base64_encoded_image = ImageEncoderService.encode_image_to_base64(image_to_llm)

        mime_type = "image/jpeg"
        if isinstance(image_to_llm, str):
            mime_type = ImageEncoderService.get_mime_type(image_to_llm)

        response = self._client.chat.completions.create(
            model=settings.vision_model,
            messages=[
                {
                    "role": "user",
                    "content":[
                        {
                            "type": "text",
                            "text":prompt
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:{mime_type};base64,{base64_encoded_image}"
                            }
                        }
                    ]
                }
            ],
        )

        return response.choices[0].message.content


