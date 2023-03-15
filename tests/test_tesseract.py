import pytest
from ocr import Tesseract
import pandas


def test_tesseract():
    image_uri = 'https://iiif-cloud.princeton.edu/iiif/2/9d%2F50%2F9a%2F9d509abf80ed4021a22f13b03f509bba%2Fintermediate_file/full/1000,/0/default.jpg'
    ocr = Tesseract(image_uri)
    result = ocr.string
    assert result.__class__ == str
    # assert ocr.alto.__class__ == str
    # assert ocr.hocr.__class__ == str
    # assert ocr.data_frame.__class__ == pd.core.frame.DataFrame
