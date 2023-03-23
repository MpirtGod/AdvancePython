import shlex
import subprocess
from datetime import timedelta
from typing import Optional
from flask import Flask, request
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

@app.route("/uptime")
def uptime():
    with open('/proc/uptime', 'r') as f:
        seconds = float(f.readline().split()[0])
    uptime = str(timedelta(seconds=seconds)).split('.')[0]
    return f"Current uptime is {uptime}"

@app.route("/ps", methods=['GET'])
def _ps():
    args: list[str] = request.args.getlist('arg')
    clean_user_cmd = [shlex.quote(arg) for arg in args]
    command_str = f"ps {' '.join(clean_user_cmd)}"
    command = shlex.split(command_str)
    result = subprocess.run(command, capture_output=True)
    if result.returncode != 0:
        return 'Что-то пошло не так!', 500
    output = result.stdout.decode()
    return f"<pre>{output}</pre>"

if __name__ == '__main__':
    app.config['WTF_CSRF_ENABLED'] = False
    app.run(debug=True)
