from google import genai
from google.genai import types
import logging
from models.config import config as app_config

logger = logging.getLogger(__name__)

client = genai.Client(api_key=app_config['GEMINI_API_KEY'])

tools = [
    types.Tool(google_search=types.GoogleSearch()),
]

safety_settings = [
    types.SafetySetting(
        category=types.HarmCategory.HARM_CATEGORY_HATE_SPEECH,
        threshold=types.HarmBlockThreshold.BLOCK_NONE
    ),
    types.SafetySetting(
        category=types.HarmCategory.HARM_CATEGORY_HARASSMENT,
        threshold=types.HarmBlockThreshold.BLOCK_NONE
    ),
    types.SafetySetting(
        category=types.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
        threshold=types.HarmBlockThreshold.BLOCK_NONE
    ),
    types.SafetySetting(
        category=types.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
        threshold=types.HarmBlockThreshold.BLOCK_NONE
    ),
]

config = types.GenerateContentConfig(
    system_instruction=app_config['SYSTEM_INSTRUCTION'],
    thinking_config=types.ThinkingConfig(
        thinking_budget=0,
    ),
    tools=tools,
    temperature=1.0,
    safety_settings=safety_settings,
)

async def run_gemini(content: str):
    model = app_config['GEMINI_MODEL']
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=content),
            ],
        ),
    ]

    response = client.models.generate_content(
        model=model,
        contents=contents,
        config=config,
    )
    logger.info("Response successful")
    return response.text