from flask import Flask, request, jsonify, send_from_directory
from werkzeug.utils import secure_filename
from flask_cors import CORS
from whisper_utils import transcribe_audio
from gpt_utils import analyze_audio
import os

app = Flask(__name__, static_folder="../frontend", static_url_path="/")
CORS(app)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")

@app.route("/upload", methods=["POST"])
def upload_audio():
    file = request.files['file']
    filename = secure_filename(file.filename)
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    file.save(filepath)

    transcript = transcribe_audio(filepath)
    result = analyze_audio(transcript)

    return jsonify({
        "transcript": transcript,
        "analysis": result
    })

if __name__ == "__main__":
    app.run(debug=True)
