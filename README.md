# Voice to Draw App with Generative AI

Bu uygulama, ses komutlarını kullanarak çizim yapmanızı sağlayan bir generatif yapay zeka uygulamasıdır. Kullanıcılar sesli komutlar vererek çeşitli çizimler oluşturabilir ve bu çizimleri uygulama aracılığıyla görüntüleyebilir.

## Gereksinimler

Bu projeyi çalıştırmak için aşağıdaki araçlara ve kütüphanelere ihtiyaç duyulmaktadır:

- Python 3.7+
- [Streamlit](https://streamlit.io/)
- OpenAI API anahtarı


## Kurulum Adımları
### 1. Repoyu Klonlayın
Bu repoyu yerel makinenize klonlayın:

    git clone https://github.com/omrrylmaz/voice_to_draw_app_with_gen_ai.git
cd voice_to_draw_app_with_gen_ai


### 2. Sanal Ortam Oluşturun ve Etkinleştirin

    
    python -m venv venv
    venv\Scripts\activate 



### 3. Bağımlılıkları Yükleyin
Gerekli bağımlılıkları yüklemek için aşağıdaki komutu çalıştırın:

    
    pip install -r requirements.txt

### 4. OpenAI API, google API Anahtarınızı Ayarlayın
OpenAI API ve Google API anahtarınızı alın ve bir ortam değişkeni olarak ayarlayın

### 5. Streamliti Çalıştırın
    
    streamlit run app.py
  
Tarayıcınızda açılan sayfada uygulamayı kullanmaya başlayabilirsiniz.

## Dosya Yapısı
app.py: Ana uygulama dosyası, Streamlit arayüzünü çalıştırır.

transcriptor.py: OpenAI Whisper API'si ile ses dosyalarını metne çevirir.

recorder.py: Ses kaydetme işlemleriyle ilgilenir.

painter.py: Sesli komutlara göre çizim oluşturma işlevlerini içerir.

requirements.txt: Proje için gerekli bağımlılıkları içerir.

icons/: Uygulama içinde kullanılan ikonları içerir.
