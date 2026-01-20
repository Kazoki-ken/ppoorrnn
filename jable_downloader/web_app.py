from flask import Flask, render_template, request, redirect, url_for, flash
import subprocess
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
            # We will use the jable_downloader's main.py to download
            # Running it as a subprocess to keep it simple.
            # Note: This might block the web server until download completes,
            # which is fine for a local single-user tool.

            # The original main.py asks for input if no args are given, so we pass url via args if possible
            # OR we can import download function. Importing is better if it doesn't have side effects.
            # Let's try to run via subprocess to ensure environment isolation and stability.

            command = f"python main.py --url {video_url}"
            process = subprocess.Popen(command, shell=True, cwd=os.getcwd(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = process.communicate()

            if process.returncode == 0:
                flash(f"Yuklash boshlandi/tugadi. Terminalni tekshiring.", 'success')
            else:
                 flash(f"Xatolik: {stderr.decode('utf-8') or stdout.decode('utf-8')}", 'error')

        except Exception as e:
            flash(f"Xatolik yuz berdi: {str(e)}", 'error')

        return redirect(url_for('index'))

    return render_template('index.html')

if __name__ == '__main__':
    print(f"Veb-server ishga tushdi: http://127.0.0.1:5000")
    print(f"Videolar ushbu papkaga yuklanadi.")
    app.run(debug=True, port=5000)
