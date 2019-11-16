
# encoding: utf-8
__author__ = 'liuwangxuezhang'


from pydub import AudioSegment
from pydub.playback import play

song = AudioSegment.from_mp3("love.mp3")
backwards = song.reverse()
backwards.export("result.mp3",format="mp3")
play(backwards)