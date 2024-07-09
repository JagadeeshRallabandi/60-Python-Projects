import os
import speech_recognition as sr
import moviepy.editor as mp
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import logging

# Set up logging
logging.basicConfig(filename='video_processing.log', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Ensure the directories exist
os.makedirs('chunks', exist_ok=True)
os.makedirs('converted', exist_ok=True)

# Define the length of the video in seconds (52 minutes)
num_seconds_video = 52 * 60
print("The video is {} seconds".format(num_seconds_video))
logging.info("The video is {} seconds".format(num_seconds_video))

# Create a list of timestamps at one-minute intervals
l = list(range(0, num_seconds_video + 1, 60))

# Initialize the dictionary to store transcriptions
diz = {}

# Initialize the recognizer
r = sr.Recognizer()

for i in range(len(l) - 1):
    try:
        # Extract subclip from the video
        ffmpeg_extract_subclip("videorl.mp4", l[i] - 2 * (l[i] != 0), l[i + 1], targetname="chunks/cut{}.mp4".format(i + 1))
        logging.info(f"Extracted chunk {i + 1} from {l[i]} to {l[i + 1]} seconds.")
        
        # Load the video clip
        clip = mp.VideoFileClip(r"chunks/cut{}.mp4".format(i + 1)) 
        
        # Convert the audio of the clip to WAV format
        audio_output_path = r"converted/converted{}.wav".format(i + 1)
        clip.audio.write_audiofile(audio_output_path)
        logging.info(f"Converted audio for chunk {i + 1} to WAV format.")
        
        # Load the audio file
        audio = sr.AudioFile(audio_output_path)
        with audio as source:
            # Adjust for ambient noise and record the audio
            r.adjust_for_ambient_noise(source)
            audio_file = r.record(source)
        
        # Transcribe the audio using Google Speech Recognition
        result = r.recognize_google(audio_file)
        
        # Store the result in the dictionary
        diz['chunk{}'.format(i + 1)] = result
        print(f"Transcription for chunk {i + 1}: {result}")
        logging.info(f"Transcription for chunk {i + 1}: {result}")

    except Exception as e:
        print(f"An error occurred for chunk {i + 1}: {e}")
        logging.error(f"An error occurred for chunk {i + 1}: {e}")
        diz['chunk{}'.format(i + 1)] = None

# Save the transcriptions to a text file
with open('transcription.txt', 'w') as f:
    for chunk, transcription in diz.items():
        f.write(f"{chunk}: {transcription}\n")

# Print the final dictionary
print(diz)
logging.info("Final transcription dictionary: {}".format(diz))
