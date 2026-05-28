

VIEW WHERE YOU HAVE MANY-TO-MANY FIELDS:

    >> Without this .save_m2m(), your form in front-end will not save the many-to-many fields if they are, for example, a select-multiple field;


        if request.method == "POST":
        ...
            if form.is_valid():
                ...
                instance.save(user=user)  # Pass the user to the Form (and then to the model)!
                form.save_m2m()  # Crucial: saving many-to-many relationships!
                ...