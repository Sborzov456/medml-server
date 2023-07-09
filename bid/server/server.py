from io import BytesIO
from pathlib import Path
import os
import flask
from flask import Flask
from flask import make_response
from flask_cors import CORS
from utils.conversion import get_slide
from utils.configuration import *

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route(f'{BASE_URL_ROOT}/<path:path>.dzi')
def dzi(path:str):
    path = f'../media/{path}'
    slide = get_slide(path, SLIDE_CONFIG)
    response = make_response(slide.get_dzi('jpeg'))
    response.mimetype = 'application/xml'
    return response

@app.route(f'{BASE_URL_ROOT}/<path:path>_files/<int:level>/<int:col>_<int:row>.<format>')
def tile(path, level, col, row, format):
    path = f'../media/{path}'
    slide = get_slide(path, SLIDE_CONFIG)
    tile = slide.get_tile(level, (col, row))
    buf = BytesIO()
    tile.save(buf, format.lower())
    response = make_response(buf.getvalue())
    response.mimetype = 'image/%s' % format
    return response

if __name__ == '__main__':
    app.config["APPLICATION_ROOT"] = BASE_URL_ROOT
    app.run(host='0.0.0.0',port=8000, debug=True)


