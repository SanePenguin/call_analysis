import os
import speech_recognition as sr
from moviepy.editor import VideoFileClip

def convertMP4toWAV(file, output_folder=".", file_name=None):
    """Converts a mp4 file to WAV and saves it in the given folder

    ARGS:
        file: The file you want to convert
        output_folder(path): the folder the file will be saved
        filename(string): the name of the wav file
    """
    name = f"{os.path.splitext(os.path.basename(file))[0]}" if file_name==None else file_name

    clip = VideoFileClip(file)
    audioclip = clip.audio
    audioclip.write_audiofile(f"{output_folder}/{name}.wav")
    audioclip.close()
    clip.close()

def transcribeAudio(WAV_FILE, language="de"):
    """Returns the transcribed wav of audio file as a string.

    ARGS:
        WAV_FILE: The audio file you want to transcribe
        language: The languanges abbreviation of the languages used in the audio file
    
    """
    r = sr.Recognizer()
    with sr.AudioFile(WAV_FILE) as source:
        audio = r.listen(source)
        return r.recognize_google(audio, language=language)



if __name__ == "__main__":
    #convertRecordingsToWAV()
    #print(transcribeAudio(r'her_audios\audio0.wav'))
    convertMP4toWAV(r"recordings\sample_rec - Kopie.mp4", output_folder="./her_audios", file_name="gay")