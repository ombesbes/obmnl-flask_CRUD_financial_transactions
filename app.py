# Import libraries
from flask import Flask, request, url_for, redirect, render_template 

# Instantiate Flask functionality
app = Flask(__name__)

# Sample data
transactions = [
    {'id': 1, 'date': '2023-06-01', 'amount': 100},
    {'id': 2, 'date': '2023-06-02', 'amount': -200},
    {'id': 3, 'date': '2023-06-03', 'amount': 300}
]

# Read operation: List all transactions
@app.route('/')
def get_transactions():
    return render_template('transactions.html', transactions=transactions)

# Create operation: Display add transaction form
# Route to handle the creation of a new transaction
@app.route('/add', methods=['GET','POST'])
def add_transaction():
    # Check if the request method is POST (form submission)
    if request.method == 'POST':
        # Create a new transaction object using form field values
        transation = {
              'id': len(transactions)+1
              'date': request.form['date']
              'amount': float(request.form['amount'])
             }
        # append the new transaction to the transactions list
        transactions.append(new_transaction)
        # Redirect to the transactions list page after adding the new transaction
        return redirect(url_for('get_transactions'))
    # If the request method is GET, render the form template to display the add transaction form
    return render_template('form.html')    

# Update operation

# Delete operation

# Run the Flask app
    