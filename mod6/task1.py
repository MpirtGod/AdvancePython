import logging
from flask import Flask
from flask_wtf import FlaskForm
from wtforms import IntegerField
from wtforms.validators import InputRequired


app = Flask(__name__)
logger = logging.getLogger('divider')

class DivideForm(FlaskForm):
    a = IntegerField(validators=[InputRequired])
    b = IntegerField(validators=[InputRequired])

@app.route('/devide/', methods=["GET"])
def divide():
    form = DivideForm()

    if form.validate_on_submit():
        a, b = form.a.data, form.b.data
        logger.debug(f"Form is valid. a={a}, b={b}")
        return f'a / b = {a / b:.2f}'
    logger.error(f'Form is not valid, error={form.errors}')
    return f'Bad request', 400

@app.errorhandler(ZeroDivisionError)
def handle_exception(e: ZeroDivisionError):
    logger.exception("We are unable to divide by zero!", exc_info=e)
    return "! unable to divide by zero!", 400


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, filename='stderr.txt', format='%(asctime)s %(clientip)-15s %(user)-8s %(message)s', datefmt='%H:%M:%S')
    logger.info("Started divider server")
    app.config["WIF_CSRF_ENABLED"] = False
    app.run(debug=True)