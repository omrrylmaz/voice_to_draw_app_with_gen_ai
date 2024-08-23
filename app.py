
import streamlit as st 
import threading
import recorder 
import transcriptor 
import painter 


if "record_active" not in st.session_state: 
    st.session_state.record_active = threading.Event()
    st.session_state.recording_status = "Başlamaya Hazır"  
    st.session_state.recording_completed = False
    st.session_state.latest_image = ""
    st.session_state.massages = []
    st.session_state.frames = []

def start_recording():
    st.session_state.record_active.set()
    st.session_state.frames = []    
    st.session_state.recording_status = " * Kaydediliyor"
    st.session_state.recording_completed = False

    threading.Thread(target=recorder.record ,
                     args=(st.session_state.record_active, st.session_state.frames)).start()
    
def stop_recording():
    st.session_state.record_active.clear()
    st.session_state.recording_status = "Kayıt Durduruldu"
    st.session_state.recording_completed = True



st.set_page_config(page_title="VoiceDraw", page_icon="🎤", layout="wide")
st.image(image="./icons/mic.jpg", width=350)
st.title("Voice Draw Uygulaması")
st.divider()

col_audio , col_image = st.columns([1,4]) 

with col_audio:
    st.subheader("Ses Kaydı")
    st.divider()
    status_massage = st.info(st.session_state.recording_status)
    st.divider()

    subcol_left , subcol_right = st.columns([1,2])

    with subcol_left:
        start_button = st.button("Başla", on_click=start_recording,disabled=st.session_state.record_active.is_set())
        stop_button = st.button("Durdur", on_click=stop_recording,disabled=not st.session_state.record_active.is_set())

    with subcol_right:
        recorded_audio = st.empty()

        if st.session_state.recording_completed : 
            recorded_audio.audio(data="voice_promt.wav")
    st.divider()
    latest_image_use = st.checkbox(label="son resmi kullan")


with col_image:
    st.subheader("Resim")
    st.divider()
    
    for massage in st.session_state.massages:

        if massage["role"] == "assistant" : 
            with st.chat_message(name = massage["role"], avatar=".icons/ai_avatar.png"):
                st.Warning("iste sizin icin olustudugumuz gorsel:"),
                st.image(image = massage["content"] ,width=300)                

        elif massage["role"] == "user":
            with st.chat_message(name = massage["role"], avatar=".icons/user_avatar.png"):
                st.success(massage["content"])                

    if stop_button:
        with st.chat_message(name ="user"):
            with st.spinner("Ses Tanıma İşlemi Yapılıyor..."):
                voice_promt = transcriptor.transcribe_with_whisper(audio_file_name="voice_promt.wav")
            st.success(voice_promt)

        st.session_state.messages.append({"role":"user", "content":voice_promt})

        with st.chat_message(name = "assistant", avatar=".icons/ai_avatar.png"):
            st.warning("Resim oluşturuldu : ")
            with st.spinner("Resim Oluşturuluyor..."):

                if latest_image_use: 
                    image_file_name = painter.generate_image(image_path=st.session_state.latest_image,prompt=voice_promt)
                    st.image(image=image_file_name  , width=300)
                else : 
                    image_file_name = painter.generate_image(prompt=voice_promt)
            
            st.image(iamge=image_file_name, width=300)

            with open(image_file_name, "rb") as file : 
                st.download_button(label="Resmi İndir", data=file, file_name=image_file_name, mime="image/png")

        st.session_state.massages.append({"role":"assistant", "content":image_file_name})
        st.session_state.latest_image = image_file_name 
