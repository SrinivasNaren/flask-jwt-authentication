from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'  # secret key for signing tokens
jwt = JWTManager(app)

# Fake user "database"
users = {
    "user1": {"password": "password123"},
    "user2": {"password": "mypassword"}
}

# Login Route
@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)

    if username in users and users[username]['password'] == password:
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    return jsonify({"msg": "Bad username or password"}), 401

# Protected Notes Route
@app.route('/notes', methods=['GET', 'POST'])
@jwt_required()
def notes():
    current_user = get_jwt_identity()
    notes = {"user1": "Note 1 content", "user2": "Note 2 content"}

    if request.method == 'GET':
        return jsonify({current_user: notes.get(current_user, "No notes found.")})
    elif request.method == 'POST':
        new_note = request.json.get('note', None)
        notes[current_user] = new_note
        return jsonify({"msg": "Note added successfully."}), 200

if __name__ == '__main__':
    app.run(debug=True)
