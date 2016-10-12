from flask import Flask, render_template
import pg

db = pg.DB(dbname='phonebook_db')
app = Flask('MyPhoneBook')

contacts = db.query('select * from phonebook').namedresult()

@app.route('/')
def home():

    return render_template(
    'phonebook.html',
     contacts = contacts
    )

if __name__ == '__main__':
    app.run(debug=True)
