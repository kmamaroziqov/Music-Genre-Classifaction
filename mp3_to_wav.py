from pydub import AudioSegment
sound = AudioSegment.from_mp3("bolaligim.mp3")
sound.export("wav/bolaligim", format="wav")