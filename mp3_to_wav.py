from pydub import AudioSegment
input_file="bolaligim.mp3"
output_file="bolaligim.wav"
sound = AudioSegment.from_mp3(input_file)
sound.export(output_file, format="wav")