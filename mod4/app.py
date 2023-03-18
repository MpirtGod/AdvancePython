from typing import Optional
from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, Field, ValidationError
from wtforms.validators import InputRequired, Email, NumberRange

app = Flask(__name__)

def number_length(min: int, max: int, message: Optional[str] = None):
    def _number_length(form: FlaskForm, field: Field):
        if len(str(field.data))>max or len(str(field.data))<min:
            raise ValidationError(message=message)
    return _number_length

class NumberLength:
    def __init__(self, min: int, max: int, message: Optional[str] = None):
        self.min = min
        self.max = max
        self.message = message

    def __call__(self, form: FlaskForm, field: Field):
        if len(str(field.data))>self.max or len(str(field.data))<self.min:
            raise ValidationError(message=self.message)

class RegistrationForm(FlaskForm):
    class Meta:
        csrf = False
    email = StringField(validators=[InputRequired(), Email()])
    phone = IntegerField(validators=[InputRequired(), number_length(10, 10, 'Number is invalid'), NumberLength(10, 10, 'Number is invalid')])
    name = StringField(validators=[InputRequired()])
    address = StringField(validators=[InputRequired()])
    index = IntegerField(validators=[InputRequired()])
    comment = StringField()


@app.route('/registration', methods = ['POST'])
def registration():
    form = RegistrationForm()
    if form.validate_on_submit():
        email, phone = form.email.data, form.phone.data
        return f'Пользователь с email {email} и телефоном +7{phone} зарегестрирован!'
    return f'{form.errors}', 400


if __name__ == '__main__':
    app.config['WTF_CSRF_ENABLED'] = False
    app.run(debug=True)
