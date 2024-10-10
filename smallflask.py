from flask import Flask, render_template

# Creating a Flask application instance
app = Flask(__name__)

# Defining a route for the home page
@app.route('/')
def books():
    # Creating a list of tuples containing book titles and their respective authors
    book_list = [('Book1', 'author1'), ('Book2', 'author2'), ('Book3', 'author3')]
    
    # Rendering the 'Books.html' template and passing the 'book_list' to it
    return render_template('Books.html', books=book_list)  # Passing 'books' to the template

# Checking if the script is running directly (not imported as a module)
if __name__ == "__main__":
    # Running the application in debug mode for easier troubleshooting
    app.run(debug=True)
