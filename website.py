from flask import Flask, render_template

app = Flask(__name__, template_folder="site_templates")

@app.route("/")
def story():
    return render_template("story.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

if __name__ == "__main__":
    app.run(debug=True, port=5001)
