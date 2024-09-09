from flask import Flask, render_template
import requests

posts = requests.get('https://api.npoint.io/ffdf0a4243e5f0b163b0').json()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', data=posts)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/post/<int:index>')
def post(index):
    matching_post = None
    for post in posts:
        if post["id"] == index:
            matching_post = post
    return render_template('post.html', post=matching_post)
if __name__ == "__main__":
    app.run(debug=True)
    