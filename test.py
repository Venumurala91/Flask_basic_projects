from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def login_user():
    return render_template('login.html')

@app.route('/logout')
def logout():
    return render_template('logout.html')



if __name__ == '__main__':
    app.run(debug=True)  