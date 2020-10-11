from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/submitted', methods=['GET', 'POST'])
def form_submitted():
    if request.method == 'POST':
        form_data = request.form.to_dict()
        print(form_data)
        name = request.form['name']
        message = request.form['message']
        return render_template('submitted.html', name=name, message=message)
    return render_template('submitted.html')


# export FLASK_ENV=development
# export FLASK_APP=app.py
# pip freeze > .dependencies
