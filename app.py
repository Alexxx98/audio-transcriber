from flask import Flask, request, render_template, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
from dotenv import load_dotenv

import assemblyai as aai

import os


load_dotenv()

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), 'upload-folder')
app.config['MAX_CONTENT_LENGTH'] = 100 * 1000 * 1000 # 100MB

aai.settings.api_key = os.getenv('API_KEY')
config = aai.TranscriptionConfig(language_code='pl')
transcriber = aai.Transcriber(config=config)


@app.route('/')
def index():
    # Remove all files saved in upload folder
    for filename in os.listdir(app.config['UPLOAD_FOLDER']):
        os.remove(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    return render_template('index.html')


@app.route('/transcribe', methods=['POST'])
def transcribe():
    if request.files:
        audio_file = request.files['file']
    elif request.form:
        audio_file = request.form['file']

    transcript = transcriber.transcribe(audio_file)
    if transcript.status == aai.TranscriptStatus.error:
        return transcript.error, 400

    filename = secure_filename(audio_file.filename.split('.')[0] + '.odt')
    with open(os.path.join(app.config['UPLOAD_FOLDER'], filename), 'w') as file:
        file.write(transcript.text)

    return redirect(url_for('download', filename=filename))


@app.route('/download/<filename>')
def download(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


if __name__ == '__main__':
    app.run(port=5002, debug=True)