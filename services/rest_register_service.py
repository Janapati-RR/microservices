import uuid
from flask import jsonify, request


def register(app):
    def register_user():
        data = request.get_json()
        if not data:
            return jsonify({"error": "No JSON data provided"}), 400

        name = data.get("name")
        age = data.get("age")
        phone = data.get("phone")

        if not all([name, age, phone]):
            return jsonify({"error": "Missing name, age, or phone"}), 400

        unique_id = str(uuid.uuid4())
        return jsonify({"message": "User registered successfully", "id": unique_id}), 201

    app.add_url_rule("/register", view_func=register_user, methods=["POST"])
