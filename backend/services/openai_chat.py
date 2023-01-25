import os
import openai

from models import schemas
from dotenv import load_dotenv

load_dotenv()

# input_text = "how to be a good father?"


def ai_chat(ai_chat_create: schemas.AiChatCreate):
    openai.api_key = os.environ.get("OPENAI_API_KEY")

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=ai_chat_create.text,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )

    output_text = response.choices[0].text
    return output_text
