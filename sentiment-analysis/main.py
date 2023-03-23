from api_communication import *
import sys

filename = 'output.wav'

audio_url = upload(filename)
save_transcript(audio_url, filename)
