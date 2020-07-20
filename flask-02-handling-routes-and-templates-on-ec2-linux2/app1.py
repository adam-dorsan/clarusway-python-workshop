from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)
def evens():
    return render_template('evens.html')

if __name__ == '__main__':
    app.run(debug=True)