from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:honeybun@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

class Post(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.String(250))

    def __init__(self, title, body):
        self.title = title
        self.body = body 


 

@app.route('/addpost', methods=['POST', 'GET'])
def addpost():


    return render_template('addpost.html', title="Add A New Blog Post!")

@app.route('/', methods=['POST', 'GET'])
def index():

    post = Post.query.all()

    return render_template('blog.html',title="Build A Blog!", post=post)



if __name__ == '__main__':
    app.run()