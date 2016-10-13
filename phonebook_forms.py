from flask import Flask, render_template, request, redirect
import pg

db = pg.DB(dbname='phonebook_db')

app = Flask('MyFormApp')



@app.route('/')
def home():
    contacts = db.query('select * from phonebook').namedresult()
    return render_template(
    'phonebook.html',
     contacts = contacts,
     title='All Entries'
    )
@app.route('/update_entry')
def update_entry():
    id = request.args.get('id')
    sql = 'select * from phonebook where id = %s' % id
    result_list = db.query(sql).namedresult()
    entry = result_list[0]
    return render_template(
    'update_entry.html',
    title = 'Update Entry',
    entry = entry
    )

@app.route('/submit_update_entry', methods=['POST'])
def submit_update_form():
    id = int(request.form.get('id'))
    name = request.form.get('name')
    phone = request.form.get('phone')
    email = request.form.get('email')
    action = request.form.get('action')
    if action == 'delete':
        db.delete('phonebook', { 'id': id })
    elif action == 'update':
        db.update('phonebook',{
        'id' : id,
        'name' : name,
        'phone_number' : phone,
        'email' : email
        })
    else:
        raise Exception("I don know how to %s" % action)
    return redirect('/')


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
