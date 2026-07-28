from google import genai

from app.core.config import settings
from app.prompts.gemini_prompt import PROMPT_TEMPLATE


class GeminiService:
    def __init__(self):
        self.client = genai.Client(
            api_key=settings.GEMINI_API_KEY
        )

        self.model = "gemini-flash-latest"

    def enhance_prompt(
        self,
        product_name: str,
        description: str,
    ) -> str:
        """
        Enhance a simple product description into a detailed
        AI image generation prompt using Gemini.
        """

        prompt = PROMPT_TEMPLATE.format(
            name=product_name,
            description=description,
        )

        try:
            response = self.client.models.generate_content(
                model=self.model,
                contents=prompt,
            )

            return response.text.strip()

        except Exception as e:
            raise RuntimeError(
                f"Gemini prompt enhancement failed: {str(e)}"
            ) from e


gemini_service = GeminiService()