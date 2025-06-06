from flask import Flask,request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


students = []

def get_letter_grade(avg):
    if avg >= 90:
        return 'A'
    elif avg >= 80:
        return 'B'
    elif avg >= 70:
        return 'C'
    elif avg >= 60:
        return 'D'
    else:
        return 'F'
    


@app.route("/")
def home():
    return "API is running!"



@app.route("/students", methods=["POST"])
def add_student():
    data = request.get_json()
    name = data.get('name')
    grades = data.get('grades', [])

    if not name or len(grades) != 5:
        return jsonify({"error": "Name and exactly 5 grades are required"}), 400
    
    average = sum(grades) / len(grades)
    letter = get_letter_grade(average)


    student = {
        "name": name,
        "grades": grades,
        "average": average,
        "letter": letter
    }


    students.append(student)
    return jsonify(student), 201

@app.route("/students", methods=["GET"])
def get_students():
    return jsonify(students)





if __name__ == "__main__":
    app.run(debug=True)