from pathlib import Path
from ocr import Tesseract, ImageDb, image_db
import pandas


def test_tesseract(tmp_path):
    image_db = ImageDb(tmp_path)
    img_uri = 'https://figgy.princeton.edu/downloads/2ae6db12-575c-4708-a8a9-8b8408c171b7/file/5028e3a4-df6d-4527-b44e-db21a81324b9'
    img_id = img_uri.split('/')[-1]
    image_file = image_db.fetch(img_uri)
    tess = Tesseract()
    assert tess.data_frame(image_file).__class__ == pandas.core.frame.DataFrame
    assert tess.alto(image_file).__class__ == str
    assert tess.hocr(image_file).__class__ == str
    assert tess.string(image_file).__class__ == str
