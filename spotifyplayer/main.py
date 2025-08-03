from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    playlist_id = "4eGdSK4NssHFmeIA8KuRFk"
    return render_template("index.html", playlist_id=playlist_id)

if __name__ == "__main__":
    app.run(debug=True)
