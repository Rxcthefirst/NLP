from api_communication import *
import sys

filename = sys.argv[1]

audio_url = upload(filename)
save_transcript(audio_url, filename)
