from flask import Flask, render_template, request

PMPizza = Flask(__name__)

@PMPizza.route('/')
def index():
    return render_template('pizzahome.html')

if __name__ == '__main__':
    PMPizza.run(debug=True)
