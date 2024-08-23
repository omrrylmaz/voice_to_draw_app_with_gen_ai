import google.generativeai as genai 
import PIL.Image 
import requests 
import os 
from dotenv import load_dotenv  
from openai import OpenAI   
from io import BytesIO  
from datetime import datetime   


load_dotenv()

my_key_openai = os.getenv('openai_apikey')  

client = OpenAI(api_key = my_key_openai)


def generate_image_with_dalle(prompt):
    AI_response = client.images.generate(
        model = "dall-e-3",
        size="1024x1024",
        quality="hd",
        n = 1,
        prompt = prompt
    )

    image_url = AI_response.images[0].url

    response = requests.get(image_url)
    imaage_bytes = BytesIO(response.content)    

    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"/img/generated_image_{timestamp}.png" 

    if not os.path.existst("img"):
        os.mkdir("img") 

    with open(filename, "wb") as f:
        f.write(imaage_bytes.getbuffer())

    return filename 


my_key_google = os.getenv('google_apikey')  

genai.configure(api_key = my_key_google)    

def gemine_vision_with_local_file(image_path , prompt) : 

    multimodality_promt = f"""bu gonderdigim resmi , bazı ek yonergelerle birlikte yenidden olustumani istiyorum. bunun ıcın ilk olarak resmi son derece ayrıntılı biçimde betimle.
      daha sonra sonucunda bana verecegin metni bir yapay zeka modelinl kullnarak gorse olusturmak kullanacaggım . 
      o yuzden yanıtını son halini verirlen bunun resim uretmekte kullanıcak bir girdi yanı promt oldguna dikkate al .
        işte yonerge şöyle : {prompt}
    """

    client = genai.GenerativeModel(model_name= "gemini-pro-vision")

    source_image = PIL.Image.open(image_path)   

    AI_response = client.generate_content(

         [
             
            prompt, 
            source_image
         ]
    )

    AI_response.resolve()

    return AI_response.text

def generate_image(image_path , prompt): 
    image_based_promt = gemine_vision_with_local_file(image_path , prompt)
    filename = generate_image_with_dalle(image_based_promt)

    return filename 

