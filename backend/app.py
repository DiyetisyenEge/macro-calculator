
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    age = int(data['age'])
    weight = float(data['weight'])
    height = float(data['height'])
    gender = data['gender']
    activity = data['activity']
    goal = data['goal']

    # Placeholder formulas for simplicity
    bmr = 10 * weight + 6.25 * height - 5 * age + (5 if gender == "male" else -161)
    tdee = bmr * {"sedentary": 1.2, "light": 1.375, "moderate": 1.55, "active": 1.725}[activity]
    if goal == "lose":
        tdee -= 500
    elif goal == "gain":
        tdee += 500

    macros = {
        "calories": round(tdee),
        "protein": round(weight * 2.0),  # 2g per kg of body weight
        "carbs": round((tdee * 0.4) / 4),  # 40% of calories from carbs
        "fat": round((tdee * 0.3) / 9)  # 30% of calories from fat
    }

    return jsonify(macros)

if __name__ == '__main__':
    app.run(debug=True)
