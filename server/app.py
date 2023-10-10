from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Define hardcoded username and password for authentication
USERNAME = 'abc'
PASSWORD = '123'

@app.route('/')
def serve_index():
    return render_template('client/index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    if username == USERNAME and password == PASSWORD:
        # Authentication successful, redirect to a protected page
        return redirect(url_for('protected_page'))
    else:
        # Authentication failed, show an error message
        return "Login failed. Please check your username and password."

@app.route('/protected')
def protected_page():
    return "Welcome to the dashboard!"
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

