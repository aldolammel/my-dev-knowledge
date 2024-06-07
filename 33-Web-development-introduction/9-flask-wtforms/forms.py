from flask_wtf import FlaskForm                                                              # Install = Flask-WTF
from wtforms import StringField, SubmitField, URLField, TimeField, SelectField
from wtforms.validators import DataRequired


class CafeForm(FlaskForm):
    ico_coffee = "☕"
    ico_wifi = "💪"
    ico_power = "🔌"
    cafe = StringField("Coffee name", validators=[DataRequired()])
    geo = URLField("Location", validators=[DataRequired()])
    open = TimeField("Open at", validators=[DataRequired()])
    close = TimeField("Close at", validators=[DataRequired()])

    coffee_rating = SelectField(
        "Coffee rating",
        choices=[("", ""),
                 ("X", ico_coffee),
                 ("XX", 2*ico_coffee),
                 ("XXX", 3*ico_coffee),
                 ("XXXX", 4*ico_coffee),
                 ("XXXXX", 5*ico_coffee)],
        validators=[DataRequired()])

    wifi_rating = SelectField(
        "Wi-Fi rating",
        choices=[("", ""),
                 ("X", ico_wifi),
                 ("XX", 2*ico_wifi),
                 ("XXX", 3*ico_wifi),
                 ("XXXX", 4*ico_wifi),
                 ("XXXXX", 5*ico_wifi)],
        validators=[DataRequired()])

    power_rating = SelectField(
        "Power outlet rating",
        choices=[("", ""),
                 ("X", ico_power),
                 ("XX", 2*ico_power),
                 ("XXX", 3*ico_power),
                 ("XXXX", 4*ico_power),
                 ("XXXXX", 5*ico_power)],
        validators=[DataRequired()])

    submit = SubmitField("Add")
