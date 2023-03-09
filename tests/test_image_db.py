import pytest
from ocr import ImageDb
from pathlib import Path


def test_image_db(tmp_path):
    idb = ImageDb(tmp_path)
    img_uri = 'https://figgy.princeton.edu/downloads/2ae6db12-575c-4708-a8a9-8b8408c171b7/file/5028e3a4-df6d-4527-b44e-db21a81324b9'
    img_id = img_uri.split('/')[-1]
    local_image = tmp_path / img_id
    assert local_image.is_file() == False
    assert tmp_path.is_dir() == True
    assert idb.fetch(img_uri) == local_image
    assert local_image.is_file() == True
