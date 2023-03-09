from flask import Flask, render_template
from post import Post


app = Flask(__name__)

@app.route('/')
def home():
    post = Post()
    data = post.all_post()
    return render_template("index.html", data=data)

@app.route('/post/<int:id>')
def blog_post(id):
    post = Post()
    data = post.all_post()
    title = ''
    body = ''
    for dt in data:
        if dt['id'] == id:
            title = dt['title']
            body = dt['body']
    return render_template("post.html", title=title, body=body)

if __name__ == "__main__":
    app.run(debug=True)
