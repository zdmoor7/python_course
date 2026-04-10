import csv
import os
from dotenv import load_dotenv
from api_wrapper import AnthropicClient

load_dotenv()

# Read the CSV file
with open("sales.csv", "r") as f:
    reader = csv.reader(f)
    rows = list(reader)

# Format as a plain text table to send to Claude
csv_text = "\n".join([", ".join(row) for row in rows])

# Send to Claude for analysis
client = AnthropicClient(api_key=os.getenv("ANTHROPIC_API_KEY"))
response = client.send_message(f"""
Here is a CSV file containing sales data:

{csv_text}

Please analyse this data and provide:
1. Key trends
2. Best and worst performing months
3. Which product performs better overall
4. Any recommendations
""")

print(response)
