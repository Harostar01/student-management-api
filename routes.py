from flask import Blueprint, request, jsonify
from database import get_db_connection

student_routes = Blueprint('student_routes', __name__)

@student_routes.route('/students', methods=['GET'])
def get_students():
    conn = get_db_connection()
    students = conn.execute('SELECT * FROM students').fetchall()
    conn.close()

    return jsonify([dict(row) for row in students])


@student_routes.route('/students', methods=['POST'])
def add_student():
    data = request.get_json()

    conn = get_db_connection()
    conn.execute('INSERT INTO students (name, age) VALUES (?, ?)',
                 (data['name'], data['age']))
    conn.commit()
    conn.close()

    return jsonify({"message": "Student added"}), 201


@student_routes.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    data = request.get_json()

    conn = get_db_connection()
    conn.execute('UPDATE students SET name=?, age=? WHERE id=?',
                 (data['name'], data['age'], id))
    conn.commit()
    conn.close()

    return jsonify({"message": "Student updated"})


@student_routes.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM students WHERE id=?', (id,))
    conn.commit()
    conn.close()

    return jsonify({"message": "Student deleted"})
    return jsonify({"message": "Student updated"})

@student_routes.route('/students/<int:index>', methods=['DELETE'])
def delete_student(index):
    students.pop(index)
    return jsonify({"message": "Student deleted"})
