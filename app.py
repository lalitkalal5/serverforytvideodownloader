from flask import Flask, request, send_file
from pytube import YouTube
import os

app = Flask(__name__)
@app.route('/download', methods=['POST'])
def download_video():
    url = request.json['url']
    yt = YouTube(url)
    stream = yt.streams.filter(res="360").first()
    if stream is None:
            stream = yt.streams.first()
    file_path = stream.download(output_path='videos/')
    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    if not os.path.exists('videos'):
        os.makedirs('videos')
    app.run(debug=True ,host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))