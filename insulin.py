import os
import json
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
    prompt = f"""You are a nutrition assistant helping a Type 1 diabetic calculate insulin doses.

The user has described their meal as: "{description}"

Parse this into individual food items. For each item, estimate a realistic portion size and calculate the carbohydrate content.

Return ONLY a valid JSON array with no explanation, in this exact format:
[
  {{"food": "Apple", "quantity": "2 medium", "weight_g": 340, "carbs_per_100g": 14.0, "total_carbs_g": 47.6}},
  ...
]

Use accurate, commonly accepted carb values per 100g. Be realistic with portion sizes — e.g. "a few dates" = 3-4 dates (~30g each), "some peanut butter" = 2 tablespoons (~32g). Only return the JSON array, nothing else."""

    try:
        response = get_client().send_message(prompt)
        # Extract JSON array from anywhere in the response
        import re
        match = re.search(r'\[.*\]', response, re.DOTALL)
        if not match:
            return jsonify({"error": "Could not extract meal data"}), 500
        items = json.loads(match.group())
        return jsonify({"items": items})
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
