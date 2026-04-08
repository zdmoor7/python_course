import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

user_prompt = input("Enter your prompt: ")

response = client.chat.completions.create(
    model="gpt-4o",
    temperature=1.0,
    max_tokens=150,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": user_prompt}
    ]
)

print(response.choices[0].message.content)