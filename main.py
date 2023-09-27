import os
from moviepy.editor import VideoFileClip

def convertRecordingsToMP3(MP4FOLDER="/recordings", MP3FOLDER="/her_audios"):
    DIR_PATH = "."
    MP4FOLDER = DIR_PATH + MP4FOLDER
    MP3FOLDER = DIR_PATH + MP3FOLDER

    for i, file in enumerate(os.listdir(MP4FOLDER)):
        clip = VideoFileClip(MP4FOLDER+"/"+file)
        audioclip = clip.audio
        audioclip.write_audiofile(f"{MP3FOLDER}/audio{i}.mp3")
        audioclip.close()
        clip.close()



if __name__ == "__main__":
    convertRecordingsToMP3()