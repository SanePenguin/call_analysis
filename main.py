import os
import speech_recognition as sr
from moviepy.editor import VideoFileClip
import pandas as pd

def convertMP4toWAV(file_path, output_folder=".", file_name=None):
    """Converts a mp4 file to WAV and saves it in the given folder

    ARGS:
        file_path(str): The file you want to convert
        output_folder(str): the folder the file will be saved
        filename(str): the name of the wav file
    """
    name = f"{os.path.splitext(os.path.basename(file_path))[0]}" if file_name==None else file_name

    clip = VideoFileClip(file_path)
    audioclip = clip.audio
    audioclip.write_audiofile(f"{output_folder}/{name}.wav")
    audioclip.close()
    clip.close()

def transcribeAudio(WAV_FILE, language="de"):
    """Returns the transcribed wav of audio file as a string.

    ARGS:
        WAV_FILE(str): The audio file you want to transcribe
        language(str): The languanges abbreviation of the languages used in the audio file
    
    """
    r = sr.Recognizer()
    with sr.AudioFile(WAV_FILE) as source:
        audio = r.listen(source)
        return r.recognize_google(audio, language=language)
    

def transcribeFolder(folder_path, language="de"):
    """Returns a list containing all transcribtions from all files in the given folder

    ARGS:
        folder_path(str): The folder containing your audio files
        language(str): The languanges used in the audi files
    """
    transcribtions = []
    for file_name in os.listdir(folder_path):
        transcribtions.append(transcribeAudio(WAV_FILE=f"{folder_path}/{file_name}"))
    return transcribtions




if __name__ == "__main__":
    #convert all recordings to wav
    PATH_OF_RECORDINGS = "./recordings"
    for i, file_name in enumerate(os.listdir(PATH_OF_RECORDINGS)):
        convertMP4toWAV(file_path=f"{PATH_OF_RECORDINGS}/{file_name}", output_folder="./her_audios", file_name=f"audio{i}")
    
    #tanscribe all audios and save them in a table
    PATH_OF_HER_AUDIOS = "./her_audios"
    PATH_OF_MY_AUDIOS ="./my_audios"
    her_transcribtions, my_transcribtions = transcribeFolder(PATH_OF_HER_AUDIOS), transcribeFolder(PATH_OF_MY_AUDIOS)
    df = pd.DataFrame([her_transcribtions, my_transcribtions], columns=["Her transcribtions", "My transcribtions"])
    #save dataframe to analyse seperatly
    df.to_pickle("transcribtion_data.pkl")