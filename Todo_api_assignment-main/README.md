# Todo_api_assignment

##To setup this project in your system. You should follow these steps.
>1. Download this project in your system
>2. Open with any IDE such as VS Code
>3. Run the following command 
    >`pip install -r /path/to/requirements.txt`
>5. To create server, run following command
    >`python app.py`
  
 
##To test this API, we need Postman

    Method      Route                                     Functionality
1.  GET     ->    http://127.0.0.1:5000/               ->   It's home route just for testing purpose
2.  GET     ->    http://127.0.0.1:5000/book/list      ->   This route is come back with a list of All the tasks
3.  POST    ->    http://127.0.0.1:5000/book/add       ->   This route is used to add a book into DB, You need to send a JSON Object from Postman with paramater name, description.
4.  GET     ->    http://127.0.0.1:5000/book/<BookId>   ->  This route is used to retrieve a book that have id = BookId pass as params by the route
5.  PATCH   ->    http://127.0.0.1:5000/book/update/<bookId> -> This route is used to update status of Book
6.  DELETE  ->    http://127.0.0.1:5000/book/delete/<bookId> -> This route is used to delete a task from Db that have id = BookId



My table structure:

- id          -> Integer (Primary Key),
* name        -> String,
+ desription  -> String,
- author      -> String
