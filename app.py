import os
from flask import Flask, request, render_template
from dotenv import load_dotenv
from api_wrapper import AnthropicClient

load_dotenv()

app = Flask(__name__)
client = AnthropicClient(api_key=os.getenv("ANTHROPIC_API_KEY"))

@app.route("/", methods=["GET", "POST"])
def index():
    response = None
    prompt = None
    if request.method == "POST":
        prompt = request.form["prompt"]
        response = client.send_message(prompt)
    return render_template("index.html", prompt=prompt, response=response)

if __name__ == "__main__":
    app.run(debug=True)
