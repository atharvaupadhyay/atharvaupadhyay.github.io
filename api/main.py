from flask import *

#Defining App
app = Flask(__name__)
app._static_folder = "Static"

#Index Function
@app.route('/')
def index():
    return render_template('index.html')

#404 Page
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

#Settings
if __name__ == "__main__":
    app.run(debug=True)