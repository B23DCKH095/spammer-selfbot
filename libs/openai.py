from openai import OpenAI
import logging
from models.config import config

logger = logging.getLogger(__name__)

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=config['OPENROUTER_API_KEY'],
)

def run_openapi(content: str):
    completion = client.chat.completions.create(
    model="z-ai/glm-4.5-air:free", # fixed
    messages=[
        {
            "role": "system",
            "content": config['SYSTEM_INSTRUCTION'],
        },
        {
        "role": "user",
        "content": content
        }
    ],
    extra_body={
        "reasoning": {
            "enabled": False,
            "exclude": True
        }
    }
    )
    logger.info("Response successful")
    return completion.choices[0].message.content