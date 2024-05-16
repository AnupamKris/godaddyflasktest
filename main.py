from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        data = request.form
        files = request.files
        # save files to upload folder
        for file in files:
            print(file)
            files[file].save(f'upload/{files[file].filename}')
        return "Success"

    else:
        return render_template('index.html')
    

if __name__ == '__main__':
    app.run(debug=True)