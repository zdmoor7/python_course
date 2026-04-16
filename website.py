import os
from flask import Flask, render_template, redirect, abort

base_dir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__,
            template_folder=os.path.join(base_dir, "site_templates"),
            static_folder=os.path.join(base_dir, "static"))

BLOG_POSTS = {
    "40-se-conversations": {
        "title": "What 40 SE conversations taught me about the role",
        "category": "Writing",
    },
    "medical-writing-storytelling": {
        "title": "How medical writing made me a better technical storyteller",
        "category": "Writing",
    },
    "demo2win-takeaways": {
        "title": "Demo2Win: what I took away and what I'd add",
        "category": "Writing",
    },
    "building-portfolio-non-engineer": {
        "title": "Building a portfolio site from scratch as a non-engineer",
        "category": "Writing",
    },
}

@app.route("/")
def index():
    return render_template("index.html", posts=BLOG_POSTS)

@app.route("/projects")
def projects():
    return redirect("/#projects")

@app.route("/blog/<slug>")
def blog_post(slug):
    post = BLOG_POSTS.get(slug)
    if not post:
        abort(404)
    return render_template("blog_post.html", post=post, slug=slug)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
