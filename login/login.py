from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy user data
users = {
    "user1": "password1",
    "user2": "password2",
    'test1':'test'
}

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            # Successful login, redirect to a welcome page
            return redirect(url_for('welcome', username=username))
        else:
            # Invalid credentials, show login page again with an error message
            error = 'Invalid username or password. Please try again.'
            return render_template('login.html', error=error)
    # If GET request, just show the login page
    return render_template('login.html')

@app.route('/welcome/<username>')
def welcome(username):
    return render_template('welcome.html', username=username)

if __name__ == '__main__':
    app.run(debug=True)
