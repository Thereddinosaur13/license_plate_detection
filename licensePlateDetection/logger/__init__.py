import logging
import os
from datetime import datetime
from from_root import from_root

log_name = datetime.now().strftime("%Y_%m_%d__%H_%M_%S")
LOG = f"{log_name}.log"
logging_path = os.path.join(from_root(), "log", LOG)
os.makedirs(logging_path, exist_ok=True)
LOGFILE_PATH = os.path.join(logging_path, LOG)

logging.basicConfig(
                filename=LOGFILE_PATH, \
                format="[%(asctime)s ] %(name)s -- %(levelname)s -- %(message)s", \
                level=logging.INFO
                )


                

