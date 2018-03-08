from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!23"

@app.route('/hello/<user>')
def hello_name(user):
   return render_template('hello.html', name=user)

if __name__ == '__main__':
    app.run()
