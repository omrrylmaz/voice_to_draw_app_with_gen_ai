import pyaudio
import wave



def record(record_active,frames):
    audio = pyaudio.PyAudio()


    # start Recording
    stream = audio.open(format=pyaudio.paInt16, 
                        channels=1,
                        rate=44100,
                        input=True,
                        frames_per_buffer=1024)
    
    while record_active.is_set():
        data =stream.read(1024 , 
                    exception_on_overflow = False) # ara bellekde hata olursa kesmesin diye 
        frames.append(data) # frames listesine ses verilerini ekler


        stream.stop_stream()
        stream.close()  
        audio.terminate()   

        sound_file = wave.open("voice_promt.wav", 'wb')
        sound_file.setnchannels(1)  
        sound_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16)) 
        sound_file.setframerate(44100)
        sound_file.writeframes(b''.join(frames))
        sound_file.close()    
        



