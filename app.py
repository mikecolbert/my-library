from flask import Flask, render_template, request, redirect, url_for, flash
import requests

app = Flask(__name__)
app.config["SECRET_KEY"] = "seasdfcrasdet"

all_books = [
    {
        "book_id": 0,
        "library_user": "colbert",
        "title": "Learn Python the Hard Way",
        "author": "Zed Shaw",
        "pages": 300,
        "isbn": "978-1-449-31667-4",
        "book_type": "non-fiction",
        "date_read": "2019-01-01",
        "genre": "programming",
        "format": "paperback",
        "source": "purchased",
        "evaluation": "recommend",
        "created_date": "2023-04-02",
        "modified_date": "2023-04-02",
    },
    {
        "book_id": 1,
        "library_user": "colbert",
        "title": "Fundamentals of Data Engineering",
        "author": "Lynda Partner",
        "pages": 300,
        "isbn": "978-1-449-31667-4",
        "book_type": "non-fiction",
        "date_read": "2023-01-29",
        "genre": "data engineering",
        "format": "kindle",
        "source": "purchased",
        "evaluation": "recommend",
        "created_date": "2023-04-02",
        "modified_date": "2023-04-02",
    },
]


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/library", methods=["GET", "POST"])
def library():
    # # Retrieve data from API
    # url = "https://example.com/api/data"
    # response = requests.get(url)
    # data = response.json()

    # # Render template with data
    return render_template("library.html", books=all_books)


@app.route("/book-details/<int:book_id>", methods=["GET", "POST"])
def book_details(book_id):
    # # Retrieve data from API
    # url = f"https://example.com/api/data/{item_id}"
    # response = requests.get(url)
    # data = response.json()

    # # Render template with data
    return render_template("book-details.html", book=all_books[book_id])


@app.route("/add-book", methods=["GET", "POST"])
def add_book():
    if request.method == "POST":
        #     # Retrieve form data
        #     name = request.form["name"]
        #     description = request.form["description"]

        #     # Send data to API as JSON
        #     url = "https://example.com/api/data"
        #     data = {"name": name, "description": description}
        #     headers = {"Content-Type": "application/json"}
        #     response = requests.post(url, json=data, headers=headers)

        #     # Display flash message if successful
        #     if response.ok:
        #         flash("Record added successfully!", "success")
        #         return redirect(url_for("index"))

        #     # Display flash message if unsuccessful
        #     flash("Failed to add record.", "error")
        #     return render_template("add.html")

        # # Render form template for GET requests
        return "book add function"
    return render_template("add-book.html")


# gets book details and populates form for editing
@app.route("/edit-book/<int:book_id>", methods=["POST"])
def edit_book(book_id):
    if request.method == "POST":
        return render_template("edit-book.html", book=all_books[book_id])
        # # Retrieve data from API
        # url = f"https://example.com/api/data/{item_id}"
        # response = requests.get(url)
        # data = response.json()

    # 405 error - method not allowed
    return render_template(url_for("library"))


# updates book details by passing form data to API
@app.route("/update-book", methods=["POST"])
def update_book():
    if request.method == "POST":
        # return url_for("library")
        return "book update function"

    # 405 error - method not allowed
    return render_template(url_for("library"))


@app.route("/delete-book/<book_id>", methods=["POST"])
def delete_book(book_id):
    if request.method == "POST":
        return "book delete function"
        # # Send delete request to API
        # url = f"https://example.com/api/data/{id}"
        # response = requests.delete(url)

        # # Display flash message if successful
        # if response.ok:
        #     flash("Record deleted successfully!", "success")
        # else:
        #     flash("Failed to delete record.", "error")

        # return redirect(url_for("index"))

    # 405 error - method not allowed
    return render_template(url_for("library"))


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
