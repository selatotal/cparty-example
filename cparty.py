from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String

app = Flask(__name__)
app.config.from_envvar('CPARTY_SETTINGS', silent=True)
db = SQLAlchemy(app)

class Book(db.Model):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String(100), unique=True)
    author = Column(String(100), unique=False)

    def __repr__(self):
        return '<Book %r>' % (self.title)

@app.route('/', methods=["GET"])
def home():
    books = Book.query.all()
    return render_template('home.html', books=books)

@app.route('/', methods=["POST"])
def addUser():
    if request.form:
        book = Book(title=request.form['title'], author=request.form['author'])
        db.session.add(book)
        db.session.commit()
    return redirect('/')

if __name__ == '__main__':
    db.create_all()
    app.run(host=app.config['IP_BIND'], port=app.config['PORT'], debug=app.config['DEBUG'])

