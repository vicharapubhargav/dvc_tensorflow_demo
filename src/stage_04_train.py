from src.utils.all_utils import read_yaml, create_directory
import argparse
import os
import logging

log_string = "[%(asctime)s: %(levelname)s: %(module)s]: %(message)s"
logs_dir = "Logs"
os.makedirs(logs_dir,exist_ok=True)
logging.basicConfig(filename=os.path.join(logs_dir,"Running_Logs.log"),level=logging.INFO,format=log_string,filemode='a')




def train(config_path,params_path):
    config = read_yaml(config_path)
    params = read_yaml(params_path)

    artifacts = config["artifacts"]
    artifacts_dir = artifacts["ARTIFACTS_DIR"]

   


if __name__ == '__main__':
    args = argparse.ArgumentParser()

    args.add_argument("--config", "-c", default="config/config.yaml")
    args.add_argument("--params", "-p", default="params.yaml")

    parsed_args = args.parse_args()

    try:
        logging.info(">>>>>Stage-04 Started...")
        train(config_path=parsed_args.config,params_path = parsed_args.params)
        logging.info("Stage-03 Completed , Training Completed and Model saved....<<<<<<\n")
    except Exception as e:
        raise e