import wave

obj = wave.open("sample.wav", "rb")

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



