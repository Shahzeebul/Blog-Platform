# app.py
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
posts = []

@app.route('/')
def home():
    return render_template('index.html', posts=posts)

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        posts.append({'title': title, 'content': content})
        return redirect(url_for('home'))
    return render_template('create.html')

if __name__ == '__main__':
    app.run(debug=True)
