from flask import Flask, render_template, request, redirect, url_for, flash
import yt_dlp
import os

app = Flask(__name__)
app.secret_key = 'supersecretkey'
DOWNLOAD_FOLDER = 'downloads'

if not os.path.exists(DOWNLOAD_FOLDER):
    os.makedirs(DOWNLOAD_FOLDER)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        video_url = request.form.get('video_url')
        if not video_url:
            flash('Iltimos, video linkini kiriting!', 'error')
            return redirect(url_for('index'))

        try:
            ydl_opts = {
                'outtmpl': f'{DOWNLOAD_FOLDER}/%(title)s.%(ext)s',
                'format': 'best',
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(video_url, download=True)
                filename = ydl.prepare_filename(info)
                flash(f"Video muvaffaqiyatli yuklandi: {os.path.basename(filename)}", 'success')
        except Exception as e:
            flash(f"Xatolik yuz berdi: {str(e)}", 'error')

        return redirect(url_for('index'))

    return render_template('index.html')

if __name__ == '__main__':
    print(f"Veb-server ishga tushdi: http://127.0.0.1:5000")
    print(f"Videolar '{DOWNLOAD_FOLDER}' papkasiga yuklanadi.")
    app.run(debug=True, port=5000)
