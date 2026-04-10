import os
from flask import Flask, render_template

base_dir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__,
            template_folder=os.path.join(base_dir, "site_templates"),
            static_folder=os.path.join(base_dir, "static"))

@app.route("/")
def story():
    return render_template("story.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

if __name__ == "__main__":
    app.run(debug=True, port=5001)
