from flask import Flask, render_template
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from database import db, Category, Thread, Post, init_db
from config import Config
import threading
import time
import schedule

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    init_db()

admin = Admin(app, name='Forum Admin', template_mode='bootstrap3')
admin.add_view(ModelView(Category, db.session))
admin.add_view(ModelView(Thread, db.session))
admin.add_view(ModelView(Post, db.session))

@app.route('/')
def index():
    categories = Category.query.all()
    latest_threads = Thread.query.order_by(Thread.created_at.desc()).limit(15).all()
    return render_template('index.html', categories=categories, threads=latest_threads)

@app.route('/category/<slug>')
def category(slug):
    cat = Category.query.filter_by(slug=slug).first_or_404()
    threads = Thread.query.filter_by(category_id=cat.id).order_by(Thread.last_activity.desc()).all()
    return render_template('category.html', category=cat, threads=threads)

@app.route('/thread/<slug>')
def thread(slug):
    t = Thread.query.filter_by(slug=slug).first_or_404()
    t.views += 1
    db.session.commit()
    posts = Post.query.filter_by(thread_id=t.id).order_by(Post.created_at).all()
    return render_template('thread.html', thread=t, posts=posts)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
