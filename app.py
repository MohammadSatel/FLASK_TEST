# app.py
from flask import Flask, abort
from tools.numbers import simp, comp

app = Flask(__name__)

@app.before_request
def check_rule():
    if not simp.functions_called:
        abort(403, "Cannot call functions in comp module before calling at least one function in simp module.")

@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
