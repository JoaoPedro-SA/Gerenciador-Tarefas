import os
import sys
import flask
from controller.usuario import *
from controller.agenda import *

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

app = Flask(__name__, template_folder=os.path.join('view', 'templates'))


app.register_blueprint(url)
app.register_blueprint(url2)



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)