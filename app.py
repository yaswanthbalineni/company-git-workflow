from flask import Flask, render_template, request

app = Flask(__name__)

# Sample user credentials
users = {
    "admin": "admin123",
    "yaswanth": "python123"
}

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username in users and users[username] == password:
        return f"Welcome {username}! Login Successful."

    return "Invalid username or password!"

if __name__ == '__main__':
    app.run(debug=True)