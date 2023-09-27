import os
import speech_recognition as sr
from moviepy.editor import VideoFileClip

def convertRecordingsToWAV(MP4FOLDER="/recordings", MP3FOLDER="/her_audios"):
    DIR_PATH = "."
    MP4FOLDER = DIR_PATH + MP4FOLDER
    MP3FOLDER = DIR_PATH + MP3FOLDER

    for i, file in enumerate(os.listdir(MP4FOLDER)):
        clip = VideoFileClip(MP4FOLDER+"/"+file)
        audioclip = clip.audio
        audioclip.write_audiofile(f"{MP3FOLDER}/audio{i}.wav")
        audioclip.close()
        clip.close()


def transcribeAudio(WAV_FILE, language="de"):
    r = sr.Recognizer()
    with sr.AudioFile(WAV_FILE) as source:
        audio = r.listen(source)
        return r.recognize_google(audio, language=language)



if __name__ == "__main__":
    convertRecordingsToWAV()
    print(transcribeAudio(r'her_audios\audio0.wav'))