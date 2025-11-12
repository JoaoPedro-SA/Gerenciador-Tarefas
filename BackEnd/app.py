import os
import sys
import flask
from controller.usuario import *
from controller.agenda import *
from flask_cors import CORS

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

app = Flask(__name__, template_folder=os.path.join('view', 'templates'))
CORS(app)

app.register_blueprint(url)
app.register_blueprint(url2)

from swagger import swaggerinit
from swagger.swaggerconfig import configure_swagger
configure_swagger(app)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)