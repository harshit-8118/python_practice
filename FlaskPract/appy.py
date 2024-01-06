from flask import Flask, render_template, redirect, request

friends = ["Prateek", "Suhail", "Narmita"]

# __name__ == '__main__'
app = Flask(__name__)

@app.route('/hello')
def hello():
    return "Hello world...!!"

@app.route("/")
def Home():
    return render_template('index.html', friends=friends, num=6)

@app.route("/home")
def Home_other():
    return redirect('/')

@app.route("/submit", methods=["POST"])
def submit_data():
    if request.method == 'POST':
        try:
            n1 = int(request.form['no1'])
            n2 = int(request.form['no2'])
        except ValueError:
            return "Invalid input. Please provide numeric values for 'no1' and 'no2'."

        file = request.files['userfile']
        file.save("FlaskPract/"+file.filename)
    return str(n1 + n2)


if __name__ == '__main__':
    # app.debug=True
    app.run(debug=True)


