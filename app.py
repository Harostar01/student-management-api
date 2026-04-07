from flask import Flask
from routes import student_routes
from models import create_table

app = Flask(__name__)

create_table()  # create DB table

app.register_blueprint(student_routes)

if __name__ == "__main__":
    app.run(debug=True)
