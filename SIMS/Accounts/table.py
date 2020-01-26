from flask_table import Table,Col

class Miscellaneous_table(Table):
    classes = ['table','table-hover']
    amount = Col('Amount')
    message = Col('Message')
    category = Col('Category')
    date = Col('Date')