from src.utils.all_utils import read_yaml, create_directory
from src.utils.model import load_model
from src.utils.create_callbacks import get_callbacks
from src.utils.data_management import train_valid_generator
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

    trained_model_dir = artifacts["TRAINED_MODEL_DIR"]
    create_directory([trained_model_dir])

    untrained_full_model_path = os.path.join(artifacts_dir,artifacts["BASE_MODEL_DIR"],artifacts["UPDATED_BASE_MODEL_NAME"])
    model = load_model(untrained_full_model_path)

    call_backs_dir = os.path.join(artifacts_dir,artifacts["CALLBACKS_DIR"])
    call_backs = get_callbacks(call_backs_dir)

    train_generator,valid_generator = train_valid_generator(data_dir = artifacts["DATA_DIR"],
                                            IMAGE_SIZE = params["IMAGE_SIZE"],
                                            BATCH_SIZE = params["BATCH_SIZE"],
                                            VALIDATION_SPLIT = params["VALIDATION_SPLIT"],
                                            data_augmentation = params["AUGMENTATION"])

   


if __name__ == '__main__':
    args = argparse.ArgumentParser()

    args.add_argument("--config", "-c", default="config/config.yaml")
    args.add_argument("--params", "-p", default="params.yaml")

    parsed_args = args.parse_args()

    try:
        logging.info(">>>>>Stage-04 Started...")
        train(config_path=parsed_args.config,params_path = parsed_args.params)
        logging.info("Stage-04 Completed ,Training of Model completed and saved....<<<<<<\n")
    except Exception as e:
        raise e