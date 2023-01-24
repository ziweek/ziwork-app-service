import os
import openai

from dotenv import load_dotenv

load_dotenv()

input_text = "how to be a good father?"
openai.api_key = os.environ.get("OPENAI_API_KEY")

response = openai.Completion.create(
    model="text-davinci-003",
    prompt=input_text,
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
)

output_text = response.choices[0].text
