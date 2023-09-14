from flask import Flask, render_template, request
from .currencyrate import currency_rate

app = Flask(__name__, static_folder='statics')

@app.route("/", methods=['GET', 'POST'])
def basic_calc():
    converted_amount = None
    error_message = None
    conversion_message = None
    if request.method == 'POST':
        try:
            amount = float(request.form['amount'])  # Convert input to float
            currency = request.form['currency']
            if currency in currency_rate:
                currency_rate_amount = currency_rate[currency]
                converted_amount = amount / currency_rate_amount
                conversion_message = f'NGN to {currency} using today\'s rate of {currency_rate_amount:.2f}'
            else:
                error_message = "Invalid currency selected."
                return render_template('index.html', error_message=error_message)
        except ValueError:
            error_message = "Invalid amount entered."
            return render_template('index.html', error_message=error_message)
    
    return render_template('index.html', display_result=converted_amount, error_message=error_message, conversion_message = conversion_message)

if __name__ == '__main__':
    app.run(debug=True)
