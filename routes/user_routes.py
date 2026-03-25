from flask import Flask, request, Blueprint, render_template
app = Flask(__name__)

user = Blueprint('user', __name__)

@user.route('/user')
def user_page():
    print("User page requested")
    return render_template('user.html')

@user.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return 'No file uploaded', 400

    file = request.files['file']
    file.save(f'uploads/{file.filename}')
    return f'Saved as uploads/{file.filename}'

if __name__ == "__main__":
    import os
    os.makedirs('uploads', exist_ok=True)
    app.run(debug=True)
