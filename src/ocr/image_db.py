from shutil import copyfileobj
from pathlib import Path
import requests


class ImageDb(object):
    def __init__(self, cache_dir: Path):
        self._cache = cache_dir

    def fetch(self, image_uri):
        image_id = image_uri.split('/')[-1]
        image_path = self._cache / image_id
        if not image_path.is_file():
            self.download_image(image_uri, image_path)
        return image_path

    def download_image(self, image_uri: str, image_path: Path) -> None:
        try:
            response = requests.get(image_uri, stream=True)
            response.raise_for_status()
            response.raw.decode_content = True
            with image_path.open("wb") as image_file:
                copyfileobj(response.raw, image_file)
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
