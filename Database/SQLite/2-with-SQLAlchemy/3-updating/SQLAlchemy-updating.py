"""
PERSISTENT DATA: DATABASE WITH SQLAlchemy: UPDATING

    + How to add a new entry;
    + How to edit a specific entry;

"""


@app.route("/add", methods=["GET", "POST"])
def go_add():
    if request.method == "POST":
        # CREATING A NEW RECORD:
        new_book = Book(
            # "id" is a primary-key on SQL db, then it's automatically created, not needed to be declared here.
            title=request.form["title"],
            author=request.form["author"],
            rating=request.form["rating"])
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for("go_home"))
    # If the method is "GET", show the page:
    return render_template("add.html")


@app.route("/edit", methods=["GET", "POST"])
def go_edit():
    if request.method == "POST":
        # UPDATING A RECORD BY PRIMARY KEY:
        book_id = request.form["id"]  # because when POST, it's not allow to request the value from URL (get method).
        book_to_update = db.get_or_404(Book, book_id)  # or 'var = Book.query.get(book_id)'
        book_to_update.title = request.form["title"]
        book_to_update.author = request.form["author"]
        book_to_update.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for("go_home"))
    # If the method is "GET", do it:
    book_id = request.args.get("id")  # requesting the id through the URL (get method)
    book_selected = db.get_or_404(Book, book_id)  # or 'var = Book.query.get(book_id)'
    return render_template("edit.html", book=book_selected)
