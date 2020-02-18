#-------------------------------------
#Video Spliter
#Copyright (c) 2020 MMLAB
#Written by
#-------------------------------------

import cv2
import os
import logging
logger = logging.getLogger(__name__ + '.spliter')

def split_video(input_path, output_path, fps, output_frame_name_format):
    """Load and split input video into frames
    Number of frame equal length of input video device by fps
    
    Input:
        input_path: str
                Video input path
        output_path: str
                Folder for store frame output
        fps: int
                Number of frame per second after split
        output_frame_name_format: str
                Output filename format
    Return:
        None
    Author:
    Last modified: 15/48_02/18/20
    """
    #Get video info
    input_video = cv2.VideoCapture(input_path);
    input_video_fps = input_video.get(cv2.CAP_PROP_FPS)
    input_video_length = int(input_video.get(cv2.CAP_PROP_FRAME_COUNT))
    logger.info("input_video_fps: " + str(input_video_fps))
    #Start split video
    logger.info("Spliter started")
    frame_count = 0
    while(input_video.isOpened() and frame_count < input_video_length):
        print("processed frame: ", str(frame_count), "/", str(input_video_length))
        ret, frame = input_video.read()
        if frame_count%(input_video_fps/fps) == 0:
            cv2.imwrite(os.path.join(output_path, 
                                    output_frame_name_format+
                                    str(frame_count)+".jpg"),
                                    frame)
        frame_count += 1
    print("split done")
    logger.info("Spliter done")
    



