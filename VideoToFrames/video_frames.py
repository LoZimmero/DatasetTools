import cv2
import sys

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
        cv2.imwrite("frames/frame%d.jpg" % count, image)     # save frame as JPEG fie. NOT NEED THIS!
        success, image = vidcap.read()
        if success:
            frames.append(image)
            current_frame += frame_interval
            vidcap.set(1, current_frame)
        #print ('Read a new frame: ', success)
        count += 1
    return frames

if __name__ == "__main__":
    frames = get_frames(sys.argv[1], sys.argv[2])

