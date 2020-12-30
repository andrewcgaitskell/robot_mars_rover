import speech_recognition as sr
#Obtain audio from microphone
r = sr.Recognizer()
# devicde_index is the index of the audio input device, if you don’t specify it, the microphone is used as the audio source by default.
# sample_rate sets the number of samples collected per second, if you don’t specify it, it will automatically be determined by the microphone of the system.
# If the setting is higher, you can get better audio quality, but it will slow down the recognition speed, and the cpu of some raspberry pie cannot keep up
with sr.Microphone(device_index=2, sample_rate=48000) as source:
r.record(source, duration=2) # 2 seconds of audio will be recorded starting from the audio source audio = r.listen(source) # Obtain the single phrase recorded by source
 
  
 124
try:
# Use CMU Sphinx to perform audio to perform speech recognition
command = r.recognize_sphinx( audio,
# Specify keywords, each keyword is a tuple with the length of 2
# The first element of the tuple is the keyword, and the second element is the sensitivity of the recognizer to this keyword(0~1)
keyword_entries=[ ('forward', 1.0), ('backward', 1.0), ('left', 1.0), ('right', 1.0), ('stop', 1.0)
] )
print(command)
# If the specified keyword cannot be recognized, an UnknowValueError exception will be poped except sr.UnknowValueError:
print('say again')
