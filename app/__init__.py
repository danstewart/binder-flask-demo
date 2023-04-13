from flask.app import Flask
from app.db import db
from app.models import User, Post


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/binder-flask-demo.db"
    db.init_app(app)

    with app.app_context():
        db.create_all()

    @app.get("/")
    def index():
        from flask import render_template

        users = db.session.query(User).all()

        return render_template("pages/index.html.j2", users=users)

    @app.get("/frames/post/<int:post_id>")
    def show_post(post_id: int):
        from flask import render_template

        post = db.get_or_404(Post, post_id)

        return render_template("frames/post.html.j2", post=post)

    @app.route("/frames/post/edit/<int:post_id>", methods=["GET", "POST"])
    def edit_post(post_id: int):
        from flask import render_template, request, redirect

        post = db.get_or_404(Post, post_id)

        if request.method == "POST":
            post.content = request.form["contents"]
            db.session.commit()
            return redirect("/frames/post/{}".format(post_id))

        return render_template("frames/post_edit.html.j2", post=post)

    @app.delete("/frames/post/delete/<int:post_id>")
    def delete_post(post_id: int):
        post = db.get_or_404(Post, post_id)
        db.session.delete(post)

        return "", 204

    return app
