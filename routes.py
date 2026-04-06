from flask import Blueprint, request, jsonify
from models import students

student_routes = Blueprint('student_routes', __name__)

@student_routes.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)

@student_routes.route('/students', methods=['POST'])
def add_student():
    data = request.get_json()
    students.append(data)
    return jsonify({"message": "Student added"}), 201

@student_routes.route('/students/<int:index>', methods=['PUT'])
def update_student(index):
    data = request.get_json()
    students[index] = data
    return jsonify({"message": "Student updated"})

@student_routes.route('/students/<int:index>', methods=['DELETE'])
def delete_student(index):
    students.pop(index)
    return jsonify({"message": "Student deleted"})
