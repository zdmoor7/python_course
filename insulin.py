import os
from flask import Flask, render_template, send_from_directory

base_dir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__,
            template_folder=os.path.join(base_dir, "insulin_templates"),
            static_folder=os.path.join(base_dir, "insulin_static"))

@app.route("/")
def index():
    return render_template("insulin.html")

@app.route("/manifest.json")
def manifest():
    return send_from_directory(base_dir, "manifest.json")

@app.route("/sw.js")
def service_worker():
    return send_from_directory(base_dir, "sw.js")

if __name__ == "__main__":
    app.run(debug=True, port=5002)
