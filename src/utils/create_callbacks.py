
import tensorflow as tf
import joblib
import os
import logging
from src.utils.all_utils import get_timestamp

def create_and_save_tensorboard_callback(tensorboard_log_dir,callbacks_dir):
    unique_name = get_timestamp("tb_logs")
    
    tb_running_logs_dir = os.path.join(tensorboard_log_dir,unique_name)
    tb_callback = tf.keras.callbacks.TensorBoard(log_dir=tb_running_logs_dir)

    tb_callback_filepath = os.path.join(callbacks_dir,"tensorboard_cb.cb")
    joblib.dump(tb_callback,tb_callback_filepath) 
    logging.info(f"Tensorboard callbacks being saved at{tb_callback_filepath}")

    
    
    
def create_and_save_checkpoint_callback(checkpoint_dir,callbacks_dir):
    checkpoint_file_path = os.path.join(checkpoint_dir,"Ckpt_model.h5")
    checkpoint_callbacks = tf.keras.callbacks.ModelCheckpoint(filepath =checkpoint_file_path,save_best_only=True) 

    checkpoint_callbacks_filepath = os.path.join(callbacks_dir,"checkpoint_cb.cb")
    joblib.dump(checkpoint_callbacks,checkpoint_callbacks_filepath)
    logging.info(f"Checkpoint callback saved at {checkpoint_callbacks_filepath}")


def get_callbacks(call_backs_dir):
    call_backs_path = [os.path.join(call_backs_dir,bin_file) for bin_file in os.listdir(call_backs_dir) if bin_file.endswith('.cb') ]

    call_backs = [joblib.load(path) for path in call_backs_path]
    
    logging.info(f"Saved Call Backs are loaded from {call_backs_dir}")
    return call_backs