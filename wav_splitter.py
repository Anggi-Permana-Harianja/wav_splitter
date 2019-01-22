'''
.wav spliter into 1 seconds tracks using python
'''
from pydub import AudioSegment
from pydub.utils import make_chunks

my_audio = AudioSegment.from_file('./trump/trump_voice.wav')
chunk_length_ms = 1000 #miliseconds
chunks = make_chunks(my_audio, chunk_length_ms) #make a one-second chunks

for i, chunk in enumerate(chunks):
	chunk_name = 'trump_hash_{0}.wav'.format(i)
	print('exporting: {}'.format(chunk_name))
	chunk.export('./trump/' + chunk_name, format = 'wav')