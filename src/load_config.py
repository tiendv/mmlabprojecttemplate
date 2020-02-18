#-------------------------------------
#Video Spliter
#Load config module
#Copyright (c) 2020 MMLAB
#Written by
#-------------------------------------

import os
from configparser import SafeConfigParser

def load_config():
    """Load all paramenter for project
    
    Input:
        None
    Return:
        input_path: str
                Video input path
        output_path: str
                Folder for store frame output
        fps: int
                Number of frame per second after split
        output_frame_name_format: str
                Output filename format
                Ex: SampleVideo_5fps_5023.jpg
    Author:
    Last modified: 15/28_02/18/20
    """
    
    config = SafeConfigParser()
    config.read("config/main.cfg")
    input_path = str(config.get('main', 'input_path'))
    output_path = str(config.get('main', 'output_path'))
    fps = int(config.get('main', 'fps'))
    output_frame_name_format = str(config.get('main', 'output_frame_name_format'))
    return input_path, output_path, fps, output_frame_name_format




