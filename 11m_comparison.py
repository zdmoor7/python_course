import os
from api_wrapper import AnthropicClient
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

anthropic_client = AnthropicClient(api_key=os.getenv("ANTHROPIC_API_KEY"))
openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

user_prompt = input("Enter your prompt: ")

anthropic_response = ___________
openai_response = openai_client.chat.completions.create(
    model="gpt-4o",
    temperature=1.0,
    max_tokens=150,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": user_prompt}
    ]
)

print("Anthropic Response:")
___________
print(print(openai_response.choices[0].message.content))
___________