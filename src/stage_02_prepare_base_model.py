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




def prepare_base_model(config_path):
    config = read_yaml(config_path)




if __name__ == '__main__':
    args = argparse.ArgumentParser()

    args.add_argument("--config", "-c", default="config/config.yaml")

    parsed_args = args.parse_args()

    try:
        logging.info(">>>>>Stage-02 Started...")
        prepare_base_model(config_path=parsed_args.config)
        logging.info("Stage-02 Completed , Base Model Created....<<<<<<\n")
    except Exception as e:
        raise e