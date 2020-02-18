#-------------------------------------
#Video Spliter
#Copyright (c) 2020 MMLAB
#Written by
#-------------------------------------
import os
import logging
import time
from src.spliter import split_video
from src.load_config import load_config
logging.basicConfig(filename=os.path.join("logs", "video_spliter_"+str(time.time())+".log"), filemode="w", level=logging.DEBUG, format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger(__name__)
    
def main():
    input_path, output_path, fps, output_frame_name_format = load_config()
    split_video(input_path, output_path, fps, output_frame_name_format)
    
if __name__ == "__main__":
    main()


