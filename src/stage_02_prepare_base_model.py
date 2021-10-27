from src.utils.all_utils import read_yaml, create_directory
from src.utils.model import get_VGG_16_model,prepare_model
import argparse
import os
import logging
import io

log_string = "[%(asctime)s: %(levelname)s: %(module)s]: %(message)s"
logs_dir = "Logs"
os.makedirs(logs_dir,exist_ok=True)
logging.basicConfig(filename=os.path.join(logs_dir,"Running_Logs.log"),level=logging.INFO,format=log_string,filemode='a')




def prepare_base_model(config_path,params_path):
    config = read_yaml(config_path)
    params = read_yaml(params_path)

    artifacts = config["artifacts"]
    artifacts_dir = artifacts["ARTIFACTS_DIR"]

    base_model_dir = artifacts["BASE_MODEL_DIR"]
    base_model_dir_path = os.path.join(artifacts_dir,base_model_dir)
    create_directory([base_model_dir])

    base_model_name = artifacts["BASE_MODEL_NAME"]
    base_model_path = os.path.join(base_model_dir_path,base_model_name)

    model = get_VGG_16_model(input_shape = params["IMAGE_SIZE"],model_path = base_model_path )
    
    full_model = prepare_model(
        model,
        CLASSES = params["CLASSES"],
        freeze_all = True,
        freeze_till = None,
        learning_rate = params["LEARNING_RATE"],
    )

    updated_model_name = artifacts["UPDATED_BASE_MODEL_NAME"]
    updated_model_path = os.path.join(base_model_dir_path,updated_model_name)

    logging.info(f"Full model Summary: \n {_model_summary(full_model)}")
    full_model.save(updated_model_path)


def _model_summary(model):
    with io.StringIO() as stream:
        model.summary(print_fn=lambda x: stream.write(f"{x}\n"))
        summary_string = stream.getvalue()
    return summary_string    



if __name__ == '__main__':
    args = argparse.ArgumentParser()

    args.add_argument("--config", "-c", default="config/config.yaml")
    args.add_argument("--params", "-p", default="params.yaml")

    parsed_args = args.parse_args()

    try:
        logging.info(">>>>>Stage-02 Started...")
        prepare_base_model(config_path=parsed_args.config,params_path = parsed_args.params)
        logging.info("Stage-02 Completed , Base Model Created....<<<<<<\n")
    except Exception as e:
        raise e