import os
import sys
import cv2

if __name__ == "__main__":
    """This function has line parameters:
        1) The input folder, containing all folders containing videos.
        2) The frame interval used to know every what frame we should take a sample from the video
    """
    input_folder = sys.argv[1]
    input_folder += "/"
    fps = int(sys.argv[2])
    count = 0
    #Check if output folder already exist
    if not os.path.isdir("output"):
        os.mkdir("output")
    for directory in os.listdir(input_folder):
        if not os.path.isdir("output/" + directory):
            os.mkdir("output/" + directory)
        if os.path.isdir(input_folder + directory):
            for video in os.listdir(input_folder + directory):
                images = get_frames(input_folder + directory + "/" + video, fps)
                for image in images:
                    cv2.imwrite("output/" + directory + "/frame%d.jpg" % count, image)
                    count += 1
        count = 0

def get_frames(video_name, frame_interval):
    """This function captures frames every frame_interval frames from video video_name"""
    #print("CV2 version: " + cv2.__version__)
    frames = []                                             #frame array to return
    current_frame = 0                                       #starting frame to capture
    count = 0                                               #number of frame captured
    frame_interval = int(frame_interval)
    vidcap = cv2.VideoCapture(video_name)
    success, image = vidcap.read()
    if success:
        frames.append(image)  
        current_frame += frame_interval
        vidcap.set(1, current_frame)
    while success:
        #cv2.imwrite("frames/frame%d.jpg" % count, image)     # save frame as JPEG fie. NOT NEED THIS!
        success, image = vidcap.read()
        if success:
            frames.append(image)
            current_frame += frame_interval
            vidcap.set(1, current_frame)
        #print ('Read a new frame: ', success)
        count += 1
    return frames