from os import path, getenv
from pathlib import Path

# tile_size + 2*overlap = 2**i !!!
SLIDE_CONFIG = {'tile_size': 510, 'overlap': 1, 'limit_bounds': True}

BASE_DIR = Path(__file__).parents[3]
MEDIA_DIR = BASE_DIR / getenv('DATA_FOLDER')
BASE_URL_ROOT = getenv('BASE_ROOT')
BASE_URL_ROOT_PATH = Path(BASE_URL_ROOT)