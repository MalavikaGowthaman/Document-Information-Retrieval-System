#import libs
import os # operating system
from pathlib import Path # to get a path and to locate the path
import logging # for logging info

# this command will show the information of asc time and message
logging.basicConfig(level=logging.INFO,format='[%(asctime)s: %(message)s]')

# list of files to be created
list_of_files =[
    "src/__init__.py", # src is an dir and inside src __init__.py is created
    "src/helper.py", # inside src helper.py is created
    ".env", # .env is created in the explorer
    "requirements.txt", 
    "setup.py",
    "app.py",
    "research/trials.ipynb", # research dir created inside that trails .ipyn created
]

# this codes to create the above mentioned files 
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir,filename = os.path.split(filepath)

# if the file dir is empty create dir
    if filedir !="":
        os.makedirs(filedir,exist_ok =True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

# if the file path is not there create and write
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    else:
        logging.info(f"{filename} is already exists")

        
