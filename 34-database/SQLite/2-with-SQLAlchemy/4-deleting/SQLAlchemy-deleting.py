"""
PERSISTENT DATA: DATABASE WITH SQLAlchemy: DELETING

    + How to delete a specific entry;
    + How to delete all entries from a specific table;

"""




@app.route("/delete")
def act_del():
    book_id = request.args.get("id")  # take the value of "id" declared in the URL.
    # DELETING A RECORD:
    book_to_delete = db.get_or_404(Book, book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for("go_home"))
