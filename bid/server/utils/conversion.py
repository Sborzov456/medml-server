from openslide.deepzoom import DeepZoomGenerator
from openslide import OpenSlide

def get_slide(path, options):
    osr = OpenSlide(path)
    return DeepZoomGenerator(osr, **options)
