from celery import shared_task
from pathlib import Path
from medml import models



# from medml.utils import sendToMl, updateClassesToGroup, updateModels, send_2_email
# from django.utils import timezone
# from django.conf import settings
# import datetime

# from medml.nn.loaders.img_loader import defaultImgLoader
# from medml.nn.defaultModels import DefalutModels
# from django.conf import settings


@shared_task
def predict_all2(file_path: str, projection_type: str, id: int):
  print('predictions')
  # nn_cls = DefalutModels['C'][projection_type]
  # nn_seg = DefalutModels['S'][projection_type]
  # img = defaultImgLoader.load(file_path)
  # mask = nn_seg.predict(img)
  # classes = nn_cls(nn_seg.rois, nn_seg.img_type)
  # with open(settings.MEDI_ROOT / 'mask.pkl', 'w') as out:
  #   import pickle
  #   pickle.dump(mask, out)
  # with open(settings.MEDI_ROOT / 'class.pkl', 'w') as out:
  #   import pickle
  #   pickle.dump(classes, out)
  # print('predicted!')
