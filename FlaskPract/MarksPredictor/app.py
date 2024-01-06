from flask import Flask, request, render_template
import joblib as jb
app = Flask(__name__)
model = jb.load('FlaskPract\MarksPredictor\model.pkl')

@app.route("/")
def Home():
    return render_template('index.html')

@app.route('/getMarks', methods=['POST'])
def marks():
    if request.method == 'POST':
        hrs = float(request.form['hours'])
        marks = str(model.predict([[hrs]])[0][0])
    return render_template('index.html', my_marks=marks)


if __name__ == '__main__':
    app.run(debug=True)
