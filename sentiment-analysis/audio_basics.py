import wave



def load_wav(file):
    """
    Utility function for loading a .wav file and using the built-n Python library to construct a new .wav
    output file.
    :param obj: object holding the binary data for the .wav file
    """
    obj = wave.open(file, "rb")
    return obj


obj = load_wav("sample.wav")

print("Number of channels", obj.getnchannels())
print("Sample width", obj.getsampwidth())
print("Number of frames", obj.getnframes())
print("Frame rate", obj.getframerate())
print("Parameters", obj.getparams())

t_audio = obj.getnframes() / obj.getframerate()  # calculate duration [ (f) / (f/s) ] = s
print(t_audio, "seconds")

frames = obj.readframes(-1)
print(type(frames), type(frames[0]))
print(len(frames))

obj_new = wave.open("sample_redux.wav", "wb")

obj_new.setnchannels(2)
obj_new.setsampwidth(2)
obj_new.setframerate(48000.0)

obj_new.writeframes(frames)

obj_new.close()



