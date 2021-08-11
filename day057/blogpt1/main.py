import requests
from flask import Flask, render_template

from post import Post


blog_posts = [
    Post(post['id'], post['body'], post['title'], post['subtitle'])
    for post
    in requests.get('https://api.npoint.io/ed99320662742443cc5b').json()
]

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html', posts=blog_posts)

@app.route('/post/<int:id>')
def read_post(id):
    post = [post for post in blog_posts if post.id == id][0]
    return render_template('post.html', post=post)


if __name__ == "__main__":
    app.run(debug=True)
