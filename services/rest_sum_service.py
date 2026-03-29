from flask import jsonify, request


def register(app):
    def add_numbers():
        try:
            num1 = float(request.args.get("num1", 0))
            num2 = float(request.args.get("num2", 0))
            return jsonify({"result": num1 + num2}), 200
        except ValueError:
            return jsonify({"error": "Invalid input. Please provide numbers."}), 400

    app.add_url_rule("/sum", view_func=add_numbers, methods=["GET"])
