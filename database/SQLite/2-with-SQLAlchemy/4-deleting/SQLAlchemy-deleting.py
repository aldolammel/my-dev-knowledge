"""
PERSISTENT DATA: DATABASE WITH SQLAlchemy: DELETING

    + How to delete a specific entry;
    + How to delete all entries from a specific table;

"""
from flask import request, jsonify


# CONSTANTS:
API_KEY = "my%S3cr3t*4P1~K3y"  # Using to protect against unwanted delete requests.


@app.route("/shop/delete/<int:shop_id>", methods=["DELETE"])
# TO TEST: In Postman or Insomnia: http://127.0.0.1:5000/shop/delete/12?api_key=abcdefgh
def delete(shop_id):
    # Take this parameter value from the URL:
    suspicious_key = request.args.get("api_key")
    # Figuring out that Coffee Shop the id belongs:
    shop = Cafe.query.get(shop_id)  # Dont use 'get_or_404()' here, otherwise you cannot test that return-error-message.
    # Checking if match the both:
    if shop:
        if suspicious_key == API_KEY:
            db.session.delete(shop)
            db.session.commit()
            return jsonify(
                response={"DONE": f"The Coffee Shop ID-{shop_id} has been deleted."}
            ), 200  # 2xx Success: 200 = OK.
        # If not match the api key:
        return jsonify(
            response={"UNAUTHORIZED": f"Make sure you're using the right API key in the URL: {API_KEY}"}
        ), 401  # 4xx Client Error: 401 = Unauthorized.
    # If shop_id doesn't exist:
    return jsonify(
        response={"ERROR": f"There's no ID-{shop_id} into the database."}
    ), 404  # 4xx Client Error: 404 = Not Found.
