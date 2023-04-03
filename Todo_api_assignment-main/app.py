from flask import Flask, jsonify, request, Response
from flask_sqlalchemy import SQLAlchemy

# create the app 
app = Flask(__name__)
app.debug = True

# create the extension
db = SQLAlchemy()

# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# initialize the app with the extension
db.init_app(app)


#create the model
class Book(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    name = db.Column(db.String(100), nullable = False)
    author = db.Column(db.String(50))
    description = db.Column(db.String())

with app.app_context():
    db.create_all()




#home route
@app.route("/")
def home():
    return "Home Page"



# get all todo list
@app.route("/book/list")
def getAllbooks():
    bookList = Book.query.all()
    result = {}
    for i in bookList:
        temp = {
            "Id" : i.id,
            "BookName" : i.name,
            "Author" : i.author,
            "Description": i.description
        }
        result[i.id] = temp
    if(result == {}):
        return "There is no task on your list"
    return jsonify(result) 


#create a todo task 
@app.route('/book/add', methods=['POST'])
def createTask():
    BookName = request.get_json().get("name")
    Author=request.get_json().get("author")
    Description = ""
    if(request.get_json().get("description") != None):
        Description = request.get_json().get("description")
    newBook = Book(name = BookName,author= Author, description = Description)
    db.session.add(newBook)
    db.session.commit()
    return "Book add successfully..."


# to get a particular book
@app.route("/book/<int:BookId>")
def getOneBook(BookId):
    book = None
    book = Book.query.get(BookId)
    if(book == None):
        return "There is no task exist with this Id"
    result = {
        "id" : book.id,
        "name" :book.name,
        "author": book.author,
        "description" : book.description
       
    }
    return jsonify(result)

#update a book task 
#mark as complete or incomplete
@app.route("/book/update/<int:BookId>", methods=['PATCH'])
def update(BookId):
    book = None
    book = Book.query.get(BookId)
    if(book== None):
        return "There is no task exist with this Id"
    book.description = "Updated Description"
    db.session.commit()
    return "Update successfully"


#delete a todo task 
@app.route("/book/delete/<int:BookId>", methods = ['DELETE'])
def deleteBook(BookId):
    book = None
    book = Book.query.get(BookId)
    if(book == None):
        return "There is no task exist with this Id"
    db.session.delete(book)
    db.session.commit()
    return "deletion done"



if __name__ == "__main__":
    app.run(port=5000)


