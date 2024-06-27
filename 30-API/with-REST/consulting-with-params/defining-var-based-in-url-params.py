"""
    HOW TO DEFINE A VARIABLE BASED AN URL PARAMETER VALUE:

    Flask Module:
        Using request.args.get()

"""
from flask import jsonify, request


@app.route("/cafe/<int:cid>", methods=["PATCH"])
def update_price(cid):
    # Take from the URL this parameter value:
    new_price = request.args.get("new_price")
    # Figuring out that Coffee the id belongs:
    cafe = db.get_or_404(Cafe, cid)
    # If cafe exists:
    if cafe:
        # Define the new value to the coffee price:
        cafe.coffee_price = new_price
        # Update it on database:
        db.session.commit()
        return jsonify(response={"DONE": f"{cafe.name} has a new price: {new_price}"})
