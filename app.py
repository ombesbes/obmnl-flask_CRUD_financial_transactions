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
        transaction = {
              'id': len(transactions)+1,
              'date': request.form['date'],
              'amount': float(request.form['amount'])
             }
        # append the new transaction to the transactions list
        transactions.append(transaction)
        # Redirect to the transactions list page after adding the new transaction
        return redirect(url_for('get_transactions'))
    # If the request method is GET, render the form template to display the add transaction form
    return render_template('form.html')    

# Update operation
@app.route('/edit/<int:transaction_id>', methods=['GET','POST'])
def edit_transaction(transaction_id):
    if request.method == 'POST':
        #find the transaction with the ID that matches transaction_id
        for i, tran in enumerate(transactions):
            if transactions[i]['id'] == transaction_id:
                ind=i
                break
        transaction = {
              'id': transaction_id,
              'date': request.form['date'],
              'amount': float(request.form['amount'])
             }
        # modify the data relevant to the transaction_id
        transactions[ind]   =transaction
        # Redirect to the transactions list page after adding the new transaction
        return redirect(url_for('get_transactions'))
    
    # If the request method is GET, find the transaction with the matching ID and render the edit form
    for transaction in transactions:
        if transaction['id'] == transaction_id:
            # Render the edit form template and pass the transaction to be edited
            return render_template("edit.html", transaction=transaction)
    # If the transaction with the specified ID is not found, handle this case (optional)
    return {"message": "Transaction not found"}, 404
     

# Delete operation: Delete a transaction
# Route to handle the deletion of an existing transaction
@app.route('/delete/<int:transaction_id>')
def delete_transaction(transaction_id):
    # Find the transaction with the matching ID and remove it from the list
    for transaction in transactions:
        if transaction['id'] == transaction_id:
            transactions.remove(transaction)  # Remove the transaction from the transactions list
            break  # Exit the loop once the transaction is found and removed
    
    # Redirect to the transactions list page after deleting the transaction
    return redirect(url_for('get_transactions'))          

#a new feature that allows users to search for transactions within a specified amount range
@app.route('/search', methods=['GET','POST'])
def search_transactions():
    if request.method == 'POST':
        min_amount = float(request.form['min_amount'])
        max_amount = float(request.form['max_amount'])
        filtered_transactions = [transaction for transaction in transactions if  min_amount <= transaction['amount'] <= max_amount]
        return render_template('transactions.html', transactions=filtered_transactions)  
    
    #If the request method is GET, render a new template called search.html
    return render_template('search.html')

#a new feature that calculates and displays the total balance of all transactions
@app.route('/balance')
def total_balance():
    su=0
    for transaction in transactions:
        su+=transaction['amount']
    return render_template('transactions.html', transactions=transactions, total_balance=su)

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)    