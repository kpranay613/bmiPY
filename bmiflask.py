from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    weight = float(request.form['weight'])
    height = float(request.form['height']) / 100
    bmi = weight / (height ** 2)

    if bmi < 18.5:
        result = "Underweight"
        image = "underweight.png"
    elif 18.5 <= bmi < 25:
        result = "Normal weight"
        image = "normal_weight.png"
    elif 25 <= bmi < 30:
        result = "Overweight"
        image = "overweight.png"
    else:
        result = "Obesity"
        image = "obesity.png"

    return render_template('result.html', bmi=bmi, result=result, image=image)

if __name__ == '__main__':
    app.run(debug=True)
