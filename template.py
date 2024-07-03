import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

my_project_name = "licensePlateDetection"

list_files = [
    "./github/workflows/.gitkeep", # Git, by default, does not track empty directories – 
                                #it doesn't add them to our repository.
                                # # .gitkeep is a way to circumvent this limitation.
    "data/.gitkeep",    # contain input img or video 
    f"{my_project_name}/__init__.py",
    f"{my_project_name}/components/__init__.py",
    f"{my_project_name}/components/data_validation.py",
    f"{my_project_name}/components/model_trainer.py",
    f"{my_project_name}/constant/__init__.py",
    f"{my_project_name}/constant/training_pipeline/__init__.py",
    f"{my_project_name}/constant/app.py",
    f"{my_project_name}/entity/config_entity.py",
    f"{my_project_name}/entity/artifacts_entity.py",
    f"{my_project_name}/exception/__init__.py",
    f"{my_project_name}/logger/__init__.py",
    f"{my_project_name}/pipeline/training_pipeline.py",
    f"{my_project_name}/utils/__init__.py",
    f"{my_project_name}/utils/main_utils.py",
    "reseach/trials.ipynb",
    "templates/index.html",
    "app.py",
    "Dockerfile",
    "requirement.txt",
    "setup.py"
    
]

for file_path in list_files:
    file_path = Path(file_path) #convert to windowpath
    file_dir, file_name = os.path.split(file_path)
    
    if file_dir != "":
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"Creating directory: {file_name} in file {file_dir}")
    if (not os.path.exists(file_name)) or (os.path.getsize(file_name)==0): #check result of creating file process
        with open(file_path, "w") as f:
            pass
            logging.info(f"Creating emty file: {file_name}")
    else:
        logging.info(f"{file_name} is already existed!")    