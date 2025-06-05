from flask import Flask,request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return "API is running!"

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
    

@app.route("/students", methods=["POST"])
def add_student():
    data = request.get_json()











if __name__ == "__main__":
    app.run(debug=True)