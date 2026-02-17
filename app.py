import os
import shutil


from flask import Flask, jsonify, request, send_file
from werkzeug.utils import secure_filename
from pathlib import Path
from flasgger import Swagger, swag_from
from swagger_config import swagger_config
from swagger_template import swagger_template
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

swagger = Swagger(app, config=swagger_config, template=swagger_template)

@app.route('/', methods=['GET'])
@swag_from('swaggerDocs/conexion.yml')
def conexion():
    try:
        return jsonify({"Mensaje": "Hola mundo"}), 200
    except Exception as e:
        return jsonify({"mensaje": "Error al conectarse al endpoint", "error": str(e)}), 500