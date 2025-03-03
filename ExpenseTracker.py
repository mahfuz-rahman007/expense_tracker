import json

class ExpenseTracker:
    
    # Add A New Expense Record
    def add_expense(self, transaction, filename = "data/expense.json"):
        expense_text = self.getExpenseFromJson(filename)
        json_string_data = self.handleAddExpenseToJson(expense_text, transaction)
        self.writeExpenseToJson(filename, json_string_data)
    
    # Handle Logic of Adding New Expense To Json File
    def handleAddExpenseToJson(self, expense_text, transaction):
        json_data = json.loads(expense_text)
        new_expense = {
            "amount": transaction.amount,
            "category": transaction.category,
            "date": transaction.date,
            "description": transaction.description,
        }
        json_data['expense'].append(new_expense)
        return json.dumps(json_data)

    # Get Expense Data From Json
    def getExpenseFromJson(self, filename):
        expenseFile = open(filename, 'rt')
        expenseText = expenseFile.read()
        expenseFile.close()
        return expenseText

    # Write Expense Data To Json
    def writeExpenseToJson(self, filename, expense_text):
        expenseFile = open(filename, 'w')
        expenseFile.write(expense_text)
        expenseFile.close()

    # Return a Expense View
    def view_expense(self, filename = "data/expense.json"):
        expense_text = self.getExpenseFromJson(filename)
        expense_array = json.loads(expense_text)
        print("#Date ----------- #Amount ------- #Category")
        for expense in expense_array['expense']:
            print(f"{expense['date']} ------  {expense['amount']}   --------- {expense['category']}")

    def filter_expense(category):
        pass

    def summarize_expenses():
        pass
    
        