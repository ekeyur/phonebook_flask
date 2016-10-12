from flask import Flask, render_template, request, redirect
import pg

db = pg.DB(dbname='phonebook_db')

app = Flask('MyFormApp')

contacts = db.query('select * from phonebook').namedresult()

@app.route('/')
def home():
    return render_template(
    'phonebook.html',
     contacts = contacts,
     title='All Entries'
    )

@app.route('/new_entry')
def new_entry_form():
    return render_template(
        'new_entry.html',
        title='New Entry')

@app.route('/submit_new_entry', methods=['POST'])
def submit_form():
    name = request.form.get('name')
    phone = request.form.get('phone_number')
    email = request.form.get('email')
    db.insert('phonebook',name=name, phone_number = phone, email = email)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
