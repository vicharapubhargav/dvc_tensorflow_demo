from src.utils.all_utils import read_yaml, create_directory
import argparse
import os
import shutil
from tqdm import tqdm
import logging

log_string = "[%(asctime)s: %(levelname)s: %(module)s]: %(message)s"
logs_dir = "Logs"
os.makedirs(logs_dir,exist_ok=True)
logging.basicConfig(filename=os.path.join(logs_dir,"Running_Logs.log"),level=logging.INFO,format=log_string,filemode='a')


def copy_file(source_download_dir,local_data_dir):
    source_files = os.listdir(source_download_dir)
    N = len(source_files)
    for file in tqdm(source_files,total=N,desc= f"Copying File from {source_download_dir} to {local_data_dir}", colour="green"):
        src = os.path.join(source_download_dir,file)
        dst = os.path.join(local_data_dir,file)
        shutil.copy(src, dst)

def get_data(config_path):
    config = read_yaml(config_path)

    source_download_dirs = config["source_download_dirs"]
    local_data_dirs = config["local_data_dirs"]

    for source_download_dir,local_data_dir in tqdm(zip(source_download_dirs,local_data_dirs),total=2,desc= "List of Folders", colour="cyan"):
        create_directory([local_data_dir])
        copy_file(source_download_dir,local_data_dir)



if __name__ == '__main__':
    args = argparse.ArgumentParser()

    args.add_argument("--config", "-c", default="config/config.yaml")

    parsed_args = args.parse_args()

    try:
        logging.info(">>>>>Stage-01 Started...")
        get_data(config_path=parsed_args.config)
        logging.info("Stage-01 Completed , Data saved into local Directory <<<<<<\n")
    except Exception as e:
        raise e