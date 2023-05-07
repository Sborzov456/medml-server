# from utils import configuration
# from random import choices
# import json

# class BoxController:
#     def __init__(self):
#         self.json = self._load_json()
#         self.keys = list(self.json.keys())

#     def _load_json(self):
#         _json = {}
#         with open(configuration.MEDIA_DIR / 'example_2.json') as inp:
#             for line in inp:
#                 _json.update(json.loads(line))
#         _json.pop('file', None)
#         _json.pop('offset', None)
#         return _json
    
#     def get_boxes(self, path:str) -> dict:
#         keys = choices(self.keys,k=100)
#         r = {k:self.json[k] for k in keys}
#         return r
    
# get_boxes = BoxController().get_boxes