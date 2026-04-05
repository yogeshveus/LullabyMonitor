from flask import Blueprint, render_template, send_from_directory
import os

recordings = Blueprint('recordings', __name__)

UPLOAD_FOLDER = "uploads"


@recordings.route('/recordings')
def view_recordings():
    files_data = []

    if os.path.exists(UPLOAD_FOLDER):
        for filename in os.listdir(UPLOAD_FOLDER):
            if filename.endswith(".wav") or filename.endswith(".webm") or filename.endswith(".mp3"):
                files_data.append({
                    "filename": filename,
                    "status": "Pending"   # Placeholder for now
                })

    # Sort latest first (optional)
    files_data.sort(key=lambda x: x["filename"], reverse=True)

    return render_template('recordings.html', files=files_data)


@recordings.route('/download/<filename>')
def download_recording(filename):
    return send_from_directory(UPLOAD_FOLDER, filename, as_attachment=True)