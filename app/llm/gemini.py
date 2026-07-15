import json
import os

from dotenv import load_dotenv
from google import genai


load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_kundali_prediction(kundali_data: dict) -> str:

    prompt = f"""
You are an expert Vedic astrology interpretation assistant.

Analyze the kundali data provided below and generate a structured
astrological interpretation.

Important rules:
- Use only the planetary and house data provided.
- Do not invent or modify planetary positions.
- Consider planets marked "Rx" as retrograde.
- Clearly explain the reasoning behind each interpretation.
- If the provided data is insufficient for a specific conclusion,
  explicitly state that instead of inventing information.
-Do not return any typography symbol (like a dot or square) for bullet points in the output. Use ony - 
- for numbering use only 1. this format for all numbers 1. 2. 3. 4. 5. 6. 7. 8. nothing else.
-at the end of your response add "- By Arjun Gupta" with left alignment 

Provide sections for:
1. Overall personality
2. Career
3. Finance
4. Relationships and marriage
5. Education
6. Strengths
7. Challenges
8. Overall outlook

Kundali data:

{json.dumps(kundali_data, indent=2)}
"""

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt,
    )

    return response.text