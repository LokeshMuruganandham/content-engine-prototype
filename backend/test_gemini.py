from app.services.gemini_service import gemini_service

result = gemini_service.enhance_prompt(
    product_name="Wooden Bowl",
    description="Handmade bowl",
)

print(result)