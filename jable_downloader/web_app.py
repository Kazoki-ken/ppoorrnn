from flask import Flask, render_template, request, redirect, url_for, flash, send_from_directory, abort
import threading
import os
import glob
# Import the download function directly
from download import download

app = Flask(__name__)
app.secret_key = 'supersecretkey'
DOWNLOAD_FOLDER = os.path.join(os.getcwd(), 'downloads')

# Make sure the download folder exists
if not os.path.exists(DOWNLOAD_FOLDER):
    os.makedirs(DOWNLOAD_FOLDER)

def run_download_in_thread(url, encode_option):
    try:
        # Save directly into the absolute DOWNLOAD_FOLDER path
        download(url, encode=encode_option, base_path=DOWNLOAD_FOLDER)
        print(f"Download completed for {url}")
    except Exception as e:
        print(f"Error downloading {url}: {e}")

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        video_url = request.form.get('video_url')
        encode_option = int(request.form.get('encode_option', 0))

        if not video_url:
            flash('Iltimos, video linkini kiriting!', 'error')
            return redirect(url_for('index'))

        # Start download in a separate thread to not block the UI
        thread = threading.Thread(target=run_download_in_thread, args=(video_url, encode_option))
        thread.start()

        flash(f"Yuklash jarayoni boshlandi! 'Videolar' bo'limini tekshiring.", 'success')
        return redirect(url_for('index'))

    return render_template('index.html')

@app.route('/list')
def list_videos():
    videos = []
    # Only scan the DOWNLOAD_FOLDER
    for item in os.listdir(DOWNLOAD_FOLDER):
        item_path = os.path.join(DOWNLOAD_FOLDER, item)
        if os.path.isdir(item_path):
            # Check if mp4 exists inside
            mp4_files = glob.glob(os.path.join(item_path, "*.mp4"))
            if mp4_files:
                for mp4 in mp4_files:
                    # videos.append({'folder': item, 'filename': os.path.basename(mp4)})
                    videos.append({
                        'folder': item,
                        'filename': os.path.basename(mp4)
                    })

    return render_template('list.html', videos=videos)

@app.route('/watch/<folder>/<filename>')
def watch_video(folder, filename):
    # Securely serve file from DOWNLOAD_FOLDER/folder/filename
    # Ensure 'folder' does not contain path traversal chars like '..'
    # Flask's send_from_directory prevents '..' in the filename, but we are constructing the directory dynamically.

    # Simple validation: ensure folder is a direct child of DOWNLOAD_FOLDER
    safe_folder_path = os.path.join(DOWNLOAD_FOLDER, folder)

    # Resolve paths to check for traversal
    try:
        safe_folder_path = os.path.realpath(safe_folder_path)
        root_path = os.path.realpath(DOWNLOAD_FOLDER)

        if not safe_folder_path.startswith(root_path):
            abort(403) # Forbidden

        if not os.path.exists(safe_folder_path):
            abort(404)

        return send_from_directory(safe_folder_path, filename)
    except Exception as e:
        print(e)
        abort(404)

@app.route('/player/<folder>/<filename>')
def player(folder, filename):
    video_src = url_for('watch_video', folder=folder, filename=filename)
    return render_template('watch.html', video_src=video_src, title=filename)

if __name__ == '__main__':
    print(f"Veb-server ishga tushdi: http://127.0.0.1:5000")
    # Debug=False for safety in production-like environments, though True is useful for development.
    # Given the user context (local helper tool), True helps debugging, but for "security fix" we can turn it off or leave it with warning.
    # We'll set it to False as per plan.
    app.run(debug=False, port=5000)
