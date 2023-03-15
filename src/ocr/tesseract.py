from io import BytesIO
import requests
import pytesseract
import pandas as pd
from PIL import Image


class Tesseract(object):
    def __init__(self, uri: str, lang="eng") -> None:
        if lang in pytesseract.get_languages():
            self.lang = lang
        else:
            raise ValueError(f'lang {lang} not found')

        self.uri = uri
        self._image = None

    @property
    def image(self):
        if self._image is None:
            response = requests.get(self.uri)
            self._image = BytesIO(response.content)
        return self._image

    @property
    def data_frame(self) -> pd.core.frame.DataFrame:
        ocr_data = pytesseract.image_to_data(
            Image.open(self.image), lang=self.lang, output_type='data.frame'
        )
        return ocr_data

    @property
    def alto(self) -> str:
        ocr_data = pytesseract.image_to_alto_xml(Image.open(self.image), lang=self.lang)

        return ocr_data.decode('UTF-8')

    @property
    def hocr(self) -> str:
        ocr_data = pytesseract.image_to_pdf_or_hocr(
            Image.open(self.image), lang=self.lang, extension='hocr'
        )
        return ocr_data.decode('UTF-8')

    @property
    def string(self) -> str:
        ocr_data = pytesseract.image_to_string(Image.open(self.image), lang=self.lang)
        return ocr_data
