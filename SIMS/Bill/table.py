from flask_table import Table,Col

class PDF_table(Table):

    classes = ['Table']
    name = Col('Name of Bill')
    date = Col('Date of Bill')
    reminder_date = Col('Date of Reminder')
