from timestamps import processed_timestamps
from moviepy import VideoFileClip
import math
import re

def video_splitting(input_video_path, timestamps_data, output_folder):
    # Load the video
    video = VideoFileClip(input_video_path)

    def final_timestamp():
        total_seconds = video.duration

        # Convert to hours, minutes, and seconds
        hours = math.floor(total_seconds // 3600)
        minutes = math.floor((total_seconds % 3600) // 60)
        seconds = total_seconds % 60

        # Display the result
        final_timestamp = f"{hours:02}:{minutes:02}:{seconds:05.2f}"
        return final_timestamp

    final_timestamp = final_timestamp()

    titles = []
    timestamps = []

    for data in timestamps_data:
        timestamps.append(timestamps_data[data])
        titles.append(data)    


    #serialise = False
    for i, title in enumerate(titles):
        start_time = timestamps[i]
        
        if i != len(titles) - 1:
            end_time = timestamps[i+1]
        else:
            end_time = final_timestamp

        title = re.sub(r'[^a-zA-Z0-9\s.]', '', title)
        
        serialise = False
        if serialise == True:
            title = f"{i}. {title}"
        elif serialise == False:
            pass

        subclip = video.subclipped(start_time, end_time)
        subclip.write_videofile(f"{output_folder}/{title}.mp4", codec='libx264')

video_path = r"D:\software\course\PyTorch for Deep Learning & Machine Learning – Full Course.mp4"
timestamps = processed_timestamps("https://www.youtube.com/watch?v=V_xro1bcAuA")
output = r"D:\software\course\course_serialised"

video_splitting(input_video_path=video_path, timestamps_data=timestamps, output_folder=output)