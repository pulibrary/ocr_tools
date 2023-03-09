from ctypes import pydll
from os import strerror
import pytesseract
from pathlib import Path
import pandas as pd


class Tesseract(object):
    def __init__(self, lang='eng') -> None:
        if lang in pytesseract.get_languages():
            self.lang = lang
        else:
            raise ValueError(f'lang {lang} not found')

    def data_frame(self, image_path: Path) -> pd.core.frame.DataFrame:
        ocr_data = pytesseract.image_to_data(
            str(image_path), lang=self.lang, output_type='data.frame'
        )
        return ocr_data

    def alto(self, image_path: Path) -> str:
        ocr_data = pytesseract.image_to_alto_xml(str(image_path), lang=self.lang)
        return ocr_data.decode('UTF-8')

    def hocr(self, image_path: Path) -> str:
        ocr_data = pytesseract.image_to_pdf_or_hocr(
            str(image_path), lang=self.lang, extension='hocr'
        )
        return ocr_data.decode('UTF-8')

    def string(self, image_path: Path) -> str:
        ocr_data = pytesseract.image_to_string(str(image_path), lang=self.lang)
        return ocr_data
