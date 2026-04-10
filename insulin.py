import os
import json
import re
from flask import Flask, render_template, send_from_directory, request, jsonify
from dotenv import load_dotenv
from api_wrapper import AnthropicClient

load_dotenv()

base_dir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__,
            template_folder=os.path.join(base_dir, "insulin_templates"),
            static_folder=os.path.join(base_dir, "insulin_static"))

def get_client():
    return AnthropicClient(api_key=os.getenv("ANTHROPIC_API_KEY"))

@app.route("/")
def index():
    return render_template("insulin.html")

@app.route("/parse-meal", methods=["POST"])
def parse_meal():
    description = request.json.get("description", "")
    context = request.json.get("context", "").strip()

    context_section = f"\nThe user has also provided this context: \"{context}\"" if context else ""

    prompt = f"""You are a clinical diabetes nutrition assistant helping a Type 1 diabetic calculate insulin doses.

The user has described their meal as: "{description}"{context_section}

Return a single JSON object with two keys:

1. "items": an array of food items in this format:
[
  {{"food": "Apple", "quantity": "2 medium", "weight_g": 340, "carbs_per_100g": 14.0, "total_carbs_g": 47.6}}
]

2. "considerations": an array of 1-4 short, specific, actionable considerations based on the meal and any context provided. Each consideration should be a plain string. Only include considerations that are genuinely relevant. Examples of the kind of thing to include:
- High fat or protein content slowing carb absorption
- Recent or planned exercise reducing insulin needs
- High GI foods causing rapid glucose spike
- Alcohol affecting glucose regulation
- Time of day effects (e.g. dawn phenomenon)

If no context was provided and the meal is straightforward, return an empty array for considerations.

Return ONLY the JSON object, no explanation."""

    try:
        response = get_client().send_message(prompt)
        match = re.search(r'\{.*\}', response, re.DOTALL)
        if not match:
            return jsonify({"error": "Could not parse meal data"}), 500
        data = json.loads(match.group())
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/manifest.json")
def manifest():
    return send_from_directory(base_dir, "manifest.json")

@app.route("/sw.js")
def service_worker():
    return send_from_directory(base_dir, "sw.js")

if __name__ == "__main__":
    app.run(debug=True, port=5002)
