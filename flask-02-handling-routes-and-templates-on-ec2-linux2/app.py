from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)
@app.route('/')
def home():
    return 'This is home page for no path, <h1> Welcome Home</h1>'
@app.route('/about')
def about():
    return '<h1>This is my about page </h1>' 
app.route('/list10')
def list10():
    return render_template('list10.html')
@app.route('/evens')
def evens():
    return render_template('evens.html')
@app.route('/error')
def error():
    return '<h1>Either you encountered an error or you are not authorized.</h1>'
@app.route('/hello')
def hello():
    return '<h1>Hello, World! </h1>' 
@app.route('/admin')
def admin(): # redirect another url
    return redirect(url_for('error'))
@app.route ('/<name>') # dynamic 
# for linking example remove greet function
def greet(name): #after 3 quote we can put html format
    greet_format=f""" 
<DOCTYPE html>
<html>
<head>
    <title>Greeting Page</title>
</head>
<body>
    <h1>Hello, {name}!</h1>
    <h2>Welcome to my Greeting Page</h2>
</body>
</html>
    """
    return greet_format
# instead of adding html to .py you my put it another
# text end link it to .py document 
@app.route('/<username>')
def anothergreat(username):
    return render_template('greet.html', name=username)
@app.route('/greet-admin')
def greet_admin(): # Dynamic Routing
    return redirect(url_for('greet', name='Master Admin'))

app.route('/evens')



if __name__ == '__main__':
    app.run(debug=True)




#    return f'<h1>Hello, {name}!</h1>' 
