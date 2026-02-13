# Imports statement - bringing in tools from Flask library
from flask import Flask, render_template, request
# Creates your Flask application
app = Flask(__name__)
# Defines a route (URL path) for the homepage, @app is a decorator. 
@app.route('/')
def index ():
    return render_template('index.html')
# Defines a route for the calculator (handles form submission)
@app.route('/calculate',methods=['POST'])
def calculate():
    #Get form data 
    revenue = float(request.form['revenue'])
    #Fixed expenses 
    truck_payment = float(request.form['truck_payment'])
    trailer_payment = float(request.form['trailer_payment'])
    insurance = float(request.form['insurance'])
    # Variable expenses
    fuel = float(request.form['fuel'])
    driver_pay = float(request.form['driver_pay'])
    factoring_percent = float(request.form['factoring_percent'])
    dispatch_percent = float(request.form['dispatch_percent'])
    repair_maintenance = float(request.form['repair_maintenance'])
    tolls = float(request.form['tolls'])
    other = float(request.form['other'])
    # Calculate
    fixed_expenses = truck_payment + trailer_payment + insurance
    factoring_amount = revenue * (factoring_percent / 100)
    dispatch_amount = revenue * (dispatch_percent / 100)
    variable_expenses = fuel + driver_pay + factoring_amount + dispatch_amount + repair_maintenance + tolls + other
    total_expenses = fixed_expenses + variable_expenses
    profit = revenue - total_expenses
    # Return results page
    return render_template('results.html', 
                         revenue=revenue,
                         fixed_expenses=fixed_expenses,
                         variable_expenses=variable_expenses,
                         total_expenses=total_expenses,
                         profit=profit)
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
    