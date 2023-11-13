from flask import Flask, render_template, request
from tools.numbers.comp import CompFunctions
from tools.numbers.simp import SimpFunctions


app = Flask(__name__)


comp = CompFunctions()
simp = SimpFunctions()


@app.route('/', methods=['GET', 'POST'])
def index():
    simp_add_result = None
    simp_subtract_result = None
    comp_sum_of_digits_result = None
    comp_is_palindrome_result = None

    if request.method == 'POST':
        if 'simp_submit' in request.form:
            # Get user input for simp module
            simp_num1 = int(request.form['simp_num1'])
            simp_num2 = int(request.form['simp_num2'])

            # Call functions from simp module
            simp_add_result = simp.add(simp_num1, simp_num2)
            simp_subtract_result = simp.subtract(simp_num1, simp_num2)

        elif 'comp_submit' in request.form:
            # Get user input for comp module
            comp_num = int(request.form['comp_num'])

            # Call functions from comp module
            comp_sum_of_digits_result = comp.sum_of_digits(comp_num)
            comp_is_palindrome_result = comp.is_palindrome(comp_num)

    return render_template('index.html', simp_add_result=simp_add_result, simp_subtract_result=simp_subtract_result,
                           comp_sum_of_digits_result=comp_sum_of_digits_result,
                           comp_is_palindrome_result=comp_is_palindrome_result)


if __name__ == '__main__':
    app.run(debug=True)
