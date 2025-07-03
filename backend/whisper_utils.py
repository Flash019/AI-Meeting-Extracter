import os 
import whisper
os.environ['PATH']+= os.pathsep+r"C:\Users\soumy\Downloads\ffmpeg-7.1.1-essentials_build\ffmpeg-7.1.1-essentials_build\bin"


model = whisper.load_model("base")

def transcribe_audio(file_path):
    result= model.transcribe(file_path)
    return result["text"]