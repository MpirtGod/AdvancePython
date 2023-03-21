import shlex
import subprocess
from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import InputRequired, NumberRange

app = Flask(__name__)
app.config["WTF_CSRF_ENABLED"] = False

class CodeForm(FlaskForm):
    code = StringField(validators=[InputRequired()])
    timeout = IntegerField(default=10, validators=[NumberRange(min=0, max=30)])

def get_result(code: str, timeout: int):
    command = f'prlimit --nproc=1:1 python3 -c "{code}"'
    command = shlex.split(command)
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    is_killed = False
    try:
        outs, errors = process.communicate(timeout=timeout)
    except subprocess.TimeoutExpired:
        process.kill()
        outs, errors = process.communicate()
        is_killed = True
    return outs.decode(), errors.decode(), is_killed

@app.route('/run_code', methods=['POST'])
def run_code():
    form = CodeForm()
    if form.validate_on_submit():
        outs, errors, is_killed = get_result(code=form.code.data, timeout=form.timeout.data)
        if is_killed:
            return f"Process was killed by timeout. Timeout={form.timeout.data}</br>{outs}</br>{errors}"
        else: return f'{outs}</br>{errors}'
    return f'Что-то пошло не так! {form.errors}', 400

if __name__ == '__main__':
    app.run()