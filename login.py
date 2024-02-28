from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)

#Home Page daripada login
@app.route('/')
def home():
    return render_template('login.html')

#Untuk mendapatkan input user dalam login
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username == " " and password == " ":
        return render_template('login.html', message='Username dan password kosong atau tidak valid!')
    else:
        return redirect(url_for('success'))

#Page jika login berhasil, maka akan berubah routingnya
@app.route('/success')
def success():
    return render_template('bs.html')

if __name__ == '__main__':
    app.run(debug=True)