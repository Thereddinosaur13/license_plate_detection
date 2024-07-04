import os.path
import sys
import yaml
import base64

from licensePlateDetection.exception import ThereddinosaurAppException
from licensePlateDetection.logger import logging

def read_yaml(file_path:str):
    try:
        with open(file_path, "rb") as yaml_file:
            logging.info(f"Read yaml file {file_path} successfully")
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise ThereddinosaurAppException(e, sys) from e
    
def write_yaml(file_path: str, content: object, replace: bool = False) -> None:
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
        
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        
        with open(file_path, "rb") as yaml_file:
            yaml.dump(content, yaml_file)
            logging.info(f"Successfully write yaml file {file_path}")
    except Exception as e:
        raise ThereddinosaurAppException(e, sys) from e
    
def decodeIamge(imgstring, file_name):
    img_data = base64.b64decode(imgstring)
    with open ("./data/" + file_name, "wb") as f:
        f.write(img_data)
        f.close()

def encodeImgIntoBase64(croppedImgPath):
    with open(croppedImgPath, "rb") as f:
        return base64.b64encode(f.read())