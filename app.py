from flask import Flask, render_template, request, redirect, url_for, flash
import requests
from datetime import datetime

app = Flask(__name__)
app.config["SECRET_KEY"] = "seasdfcrasdet"

# base url for API endpoints
api_url = "https://my-library-api.azurewebsites.net/api/v1"


# create a custom Jinja2 filter to format datetime
# {{ book.date_read | datetimeformat }} #pipe the data to the custom filter
@app.template_filter("datetimeformat")
def datetimeformat(rfc2822_value):
    # example_date = "Sat, 01 Apr 2023 22:57:51 GMT" #process with %Z
    # example_date = "Thu, 17 Mar 2022 12:34:56 +0800" #process with %z
    current_date_format = "%a, %d %b %Y %H:%M:%S %Z"
    datetime_object = datetime.strptime(  # convert string to datetime object
        rfc2822_value, current_date_format
    )
    return datetime_object.strftime("%B %d, %Y")  # convert back to string in new format


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/library", methods=["GET", "POST"])
def library():
    # Retrieve data from API for all books
    url = api_url + "/books"
    print(url)
    response = requests.get(url)
    all_books = response.json()

    if all_books:
        print("Books returned successfully.")
        print(all_books)
    else:
        print("Books not found.")

    # TODO: add error handling for API call
    # TODO: add error handling for no books returned
    # TODO: should SQL query only bring back select information? library_user, book_id, title, author

    # # Render template with data
    return render_template("library.html", books=all_books)


@app.route("/book-details/<int:book_id>", methods=["GET", "POST"])
def book_details(book_id):
    # Retrieve individual book data from API
    url = api_url + f"/book/{book_id}"
    response = requests.get(url)
    one_book = response.json()

    if one_book:
        print("Book returned successfully.")
        print(one_book)
    else:
        print("Book not found.")

    # TODO: add error handling for API call
    # TODO: add error handling for no books returned

    # # Render template with data
    return render_template("book-details.html", book=one_book)


@app.route("/add-book", methods=["GET", "POST"])
def add_book():
    if request.method == "POST":
        # Retrieve form data
        form = request.form

        # library user is a required db field. If blank, return error message.
        if not form["library_user"]:  # library user is blank
            flash("Please enter a library user.", "error")
            return redirect(url_for("add_book"))
        else:
            library_user = form["library_user"]

        # title is a required db field. If blank, return error message.
        if not form["title"]:  # title is blank
            flash("Please enter a book title.", "error")
            return redirect(url_for("add_book"))
        else:
            title = form["title"]

        author = form["author"]

        # json does not accept empty values. If pages is blank, set to None.
        if not form["pages"]:  # pages is blank
            pages = None
        else:
            pages = form["pages"]

        isbn = form["isbn"]
        book_type = form["book_type"]

        # json does not accept empty values. If date_read is blank, set to None.
        if not form["date_read"]:  # date_read is blank
            date_read = None
        else:
            date_read = form["date_read"]

        genre = form["genre"]
        format = form["format"]
        source = form["source"]
        evaluation = form["evaluation"]

        # Create dictionary of form data
        book_data = {
            "library_user": library_user,
            "title": title,
            "author": author,
            "pages": pages,
            "isbn": isbn,
            "book_type": book_type,
            "date_read": date_read,
            "genre": genre,
            "format": format,
            "source": source,
            "evaluation": evaluation,
        }

        # TODO: add error handling for API call
        # TODO: add error handling for book not inserted
        # TODO: add error handling for book already exists
        # TODO: add error handling for invalid data
        # TODO: can we capture all data into book_data, then, check it, then flash and return to add-book.html with flash message and book data so user doesnt have to retype everything?

        print(book_data)

        # Send data to API as JSON
        url = api_url + f"/books"
        print(url)
        headers = {"Content-Type": "application/json"}
        print(headers)
        response = requests.post(url, json=book_data, headers=headers)
        print(response)

        # Display flash message if successful
        if response.ok:
            print("Book added successfully!")
            # flash("Record added successfully!", "success")
            return redirect(url_for("library"))
        else:
            # Display flash message if unsuccessful
            print("Failed to add book.")
            #     flash("Failed to add record.", "error")
            return redirect(url_for("library"))

        # # Render form template for GET requests
    return render_template("add-book.html")


# gets book details and populates form for editing
@app.route("/edit-book/<int:book_id>", methods=["POST"])
def edit_book(book_id):
    if request.method == "POST":
        return render_template("edit-book.html", book=xall_books[book_id])
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


@app.route(
    "/delete-book/<book_id>", methods=["POST"]
)  # method on the front end is POST
def delete_book(book_id):
    if request.method == "POST":
        # Send delete request to API
        url = api_url + f"/book/{book_id}"
        response = requests.delete(url)  # method to the API is DELETE

        # Display flash message if successful
        if response.ok:
            print("Record deleted successfully!")
        #     flash("Record deleted successfully!", "success")
        else:
            print("Failed to delete record.")
        #     flash("Failed to delete record.", "error")

        return redirect(url_for("library"))

    # 405 error - method not allowed
    return render_template(url_for("library"))


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
