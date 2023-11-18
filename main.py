from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()


# CHAT_API_KEY = open("apikeys", "r").read()
client = OpenAI(api_key = os.getenv('OPENAI_API_KEY'))

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a fantasy football assistant, skilled in analyzing 2023 fantasy football stats to find the best players for the upcoming week."},
        {"role": "user", "content": "Who is the best wide receiver to play this week?"}
    ]
)

print(response.choices[0].message)