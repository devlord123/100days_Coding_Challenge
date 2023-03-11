from flask import Flask, render_template, request
import requests
from notification import NotificationManager

BLOG_API ='https://api.npoint.io/ab82b9ce3a3731c73269'

app = Flask(__name__)

@app.route('/')
def home():
    response = requests.get(BLOG_API)
    response.raise_for_status()
    data = response.json()
    return render_template('index.html', data=data)

@app.route('/contact', methods=["GET", "POST"])
def contact():
    error = None
    if request.method == 'POST':
        name = (request.form['name'])
        email = (request.form['email'])
        phone = (request.form['phone'])
        message = (request.form['message'])
        mail = NotificationManager()
        mail.send_mails(email,name,phone)
        return render_template('contact.html', msg_sent=True)
    else:
        error = '<h3>Error occur while connecting</h3>'
    return render_template('contact.html', msg_sent=False)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/post/<int:id>')
def post(id):
    response = requests.get(BLOG_API)
    response.raise_for_status()
    data = response.json()
    title = ''
    subtitle = ''
    body = ''
    for dt in data:
        if dt['id'] == id:
            title = dt['title']
            subtitle = dt['subtitle']
            body = dt['body']
    return render_template('post.html', title=title, subtitle=subtitle, body=body)



if __name__ == "__main__":
    app.run(debug=True)

