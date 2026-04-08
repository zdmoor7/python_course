import os
from api_wrapper import AnthropicClient
from openai import OpenAI
from dotenv import load_dotenv
import time

load_dotenv()

anthropic_client = AnthropicClient(api_key=os.getenv("ANTHROPIC_API_KEY"))
openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

user_prompt = input("Enter your prompt: ")

anthropic_start = time.time()
anthropic_response = anthropic_client.send_message(user_prompt)
anthropic_end = time.time()

openai_start = time.time()
openai_response = openai_client.chat.completions.create(
    model="gpt-4o",
    temperature=1.0,
    max_tokens=150,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": user_prompt}
    ]
)
openai_end = time.time()

print("--- Anthropic ---")
print(anthropic_response)
print(f"Time: {anthropic_end - anthropic_start:.2f} seconds")

print("--- OpenAI ---")
print(openai_response.choices[0].message.content)
print(f"Time: {openai_end - openai_start:.2f} seconds")