from io import BytesIO
from pathlib import Path
import os
import flask
from flask import Flask
from flask import make_response
from flask_cors import CORS
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
from utils.conversion import get_slide
from utils.configuration import *
# from utils.boxes import get_boxes


app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost:5432/cars_api"
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)
CORS(app, resources={r"/*": {"origins": "*"}})


@app.route(f'{BASE_URL_ROOT}/upload', methods=['POST'])
def get_image():
    image_file = flask.request.files['image']
    filename = image_file.filename
    if not filename in os.listdir(MEDIA_DIR):
        path = MEDIA_DIR / filename
        image_file.save(path)
    return filename

@app.route(f'{BASE_URL_ROOT}/<path:path>.dzi')
def dzi(path:str):
    print(f'----------------------{BASE_URL_ROOT_PATH}-----------------------')
    path = f'/{path}'
    path = Path(path).relative_to(BASE_URL_ROOT_PATH)
    cpath = MEDIA_DIR / 'svs' / path
    print(f"{cpath=}")
    slide = get_slide(cpath, SLIDE_CONFIG)
    response = make_response(slide.get_dzi('jpeg'))
    response.mimetype = 'application/xml'
    return response

@app.route(f'{BASE_URL_ROOT}/<path:path>_files/<int:level>/<int:col>_<int:row>.<format>')
def tile(path, level, col, row, format):
    path = f'/{path}'
    path = Path(path).relative_to(BASE_URL_ROOT_PATH)
    cpath = MEDIA_DIR / 'svs' / path
    slide = get_slide(cpath, SLIDE_CONFIG)
    tile = slide.get_tile(level, (col, row))
    buf = BytesIO()
    tile.save(buf, format.lower())
    response = make_response(buf.getvalue())
    response.mimetype = 'image/%s' % format
    return response

# @app.route('/<path:path>_boxes')
# def boxes(path):
#     _boxes = get_boxes(path)
#     res = make_response(_boxes)
#     return res



# from utils import models

if __name__ == '__main__':
    app.config["APPLICATION_ROOT"] = BASE_URL_ROOT
    app.run(host='0.0.0.0',port=8000, debug=True)


