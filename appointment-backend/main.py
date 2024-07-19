from fastapi import FastAPI, UploadFile, File, HTTPException,APIRouter,Form

router = APIRouter()
from fastapi.middleware.cors import CORSMiddleware
import speech_recognition as sr
from pydub import AudioSegment
import io
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from langdetect import detect, DetectorFactory
from updatejson import remove_slot
from starlette.status import HTTP_200_OK
import openai
import langcodes
import json
import csv
from deep_translator import GoogleTranslator
from korean_romanizer.romanizer import Romanizer
app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
import openai
from starlette.config import Config
config = Config(".env")
open_ai_key = config("OPEN_AI_KEY", cast=str)


# Set seed for reproducibility
DetectorFactory.seed = 0

class TranscriptionResponse(BaseModel):
    transcription: str
    translatedtext: str
    openai: str
    detectedlanguage: str
    convertedtext: str




@app.post("/transcribe/", response_model=TranscriptionResponse)
async def transcribe_audio(file: UploadFile = File(...), chathistory: str = Form(None)):
    recognizer = sr.Recognizer()
    thankyou_response = "Thank you for booking an appointment for your doctor's check-up. We are looking forward to see you. If you have any further questions or need to reschedule your appointment, please don't hesitate to contact us."   
    
    # translator = Translator()
        # languageslang=['en', 'es', 'fr', 'de', 'it', 'ko', 'fa', 'tl', 'fil']

    languages={
        'en-US': 'en', 
        'fr-FR': 'fr',
        'ko-KR': 'ko', 
        'fa-IR': 'fa', 
        'fil-PH': 'tl',
        'es-ES': 'es',
        }
    try:
        audio_data = await file.read()
        audio_file = io.BytesIO(audio_data)

        # Convert the audio file to WAV format
        audio_segment = AudioSegment.from_file(audio_file)
        wav_io = io.BytesIO()
        audio_segment.export(wav_io, format='wav')
        wav_io.seek(0)

        with sr.AudioFile(wav_io) as source:
            audio = recognizer.record(source)
            for locale,lang in languages.items():
                try:
                    transcription = recognizer.recognize_google(audio, language=locale)
                    print(transcription)
                   

                    translated_text = GoogleTranslator(source='auto', target='en').translate(transcription)
                    # Detect the language of the transcription
                    detected_language_code = detect(transcription)
                    detected_language = langcodes.Language.get(detected_language_code).display_name()

                    openairesponse =call_openai(transcription,chathistory)
                    writtentext = GoogleTranslator(source='auto', target='en').translate(openairesponse)
                    # if(openairesponse):

                    #     convertedtext= convertTextToDetectedLanguage(openairesponse,detected_language,lang)

                    

                    
                    if thankyou_response in openairesponse:
                        words=openairesponse.split()
                        day_of_appt = words[6]
                        statrt_of_appt = words[8]+" "+words[9]
                        nameofpt=words[11]
                        
                        if words[12].strip('.').isdigit():
                            contactno=words[12].strip('.')
                        else:
                            nameofpt+=" "+words[12]
                            contactno=words[13].strip('.')
                        # print("Day of appt:",day_of_appt)
                        # print("start of appt:",statrt_of_appt)
                        entry=[nameofpt,day_of_appt,statrt_of_appt,contactno]
                        
                        csv_file = '../appointment-ui/booked.csv'

                        # Read existing data from CSV
                        with open(csv_file, mode='r', newline='') as file:
                            reader = csv.reader(file)
                            data = list(reader)

                        # Add the new entry to the data
                        data.append(entry)

                        # Write the updated data back to CSV
                        with open(csv_file, mode='w', newline='') as file:
                            writer = csv.writer(file)
                            writer.writerows(data)
                        
                        remove_slot("../appointment-ui/doctor2.json",day_of_appt,statrt_of_appt)

                        
                        
                        
                        
                        
                        

                    return JSONResponse(
                    status_code=HTTP_200_OK,
                    content={"transcription": transcription,
                              "translatedtext":translated_text,
                              "openai":writtentext,
                              "detectedlanguage":detected_language,
                              "convertedtext":openairesponse}
                    )
                except sr.UnknownValueError:
                    # Continue to the next language
                    continue
            # If none of the languages were recognized
    except sr.UnknownValueError:
        raise HTTPException(status_code=400, detail="Could not understand the audio")
    except sr.RequestError as e:
        raise HTTPException(status_code=500, detail=f"Could not request results; {e}")



def convertTextToDetectedLanguage(openairesponse,detected_language,lang):

    paragraphs = openairesponse.split('\n\n')
    # Check the number of paragraphs
    number_of_paragraphs = len(paragraphs)

    translated_text = GoogleTranslator(source='auto', target=lang).translate(openairesponse)

    return translated_text


    # if(number_of_paragraphs>1):
    #     translated_text = GoogleTranslator(source='auto', target=lang).translate(paragraphs[1])
    #     if(lang == 'ko'):


    #         # Romanize Korean text to English transliteration
    #         romanized_text = Romanizer(translated_text).romanize()

    #         print(romanized_text)
    #         translated_text=romanized_text


    #     return translated_text
    # else:
    #     return ""    
         
    


def call_openai(user_prompt,chathistoryjsonstring):
# Parse the JSON string
    chat_history = json.loads(chathistoryjsonstring)


    thankyou_response = "Thank you for booking an appointment for your doctor's check-up. We are looking forward to see you. If you have any further questions or need to reschedule your appointment, please don't hesitate to contact us."   
    
    # doctor= {
    #         "id": "doc123",
    #         "name": "Dr. John Smith",
    #         "specialty": "Cardiology",
    #         "contact": {
    #         "phone": "+1234567890",
    #         "email": "dr.johnsmith@example.com"
    #         },
    #         "availability": {
    #         "weekdays": [
    #             {
    #             "day": "Monday",
    #             "slots": ["04:00-05:00", "05:00-06:00", "06:00-07:00","07:00-08:00"]
    #             },
    #             {
    #             "day": "Tuesday",
    #             "slots": ["04:00-05:00", "05:00-06:00", "06:00-07:00","07:00-08:00"]
    #             },
    #             {
    #             "day": "Wednesday",
    #             "slots": ["04:00-05:00", "05:00-06:00", "06:00-07:00","07:00-08:00"]
    #             },
    #             {
    #             "day": "Tursday",
    #             "slots": ["04:00-05:00", "05:00-06:00", "06:00-07:00","07:00-08:00"]
    #             },
    #             {
    #             "day": "Friday",
    #             "slots": ["04:00-05:00", "05:00-06:00", "06:00-07:00","07:00-08:00"]
    #             }
    #         ],
    #         "weekends": [
    #             {
    #             "day": "Saturday",
    #             "slots": ["04:00-05:00", "05:00-06:00"]
    #             }
    #         ],
    #         },
    #    }
    
    
    with open('../appointment-ui/doctor2.json', 'r') as file:
        doctor = json.load(file)

    system_prompt = """
    Role: You are a helpful appointment scheduling assistant.
    
    Objective: First, gather personal information from the user step by step .Provide a response for scheduling an appointment. After your response, provide a Thank You note related provided template.
    
    Thank You Note Template: """ + thankyou_response + """
    
    Instructions:
    
    1. Ask questions one at a time to gather personal information sequentially.
    
    2. Begin with the user's full name:
    - What is your full name?
        
    3. Then, ask for the user's contact number:
    - What is your contact number?

    4. After collecting all the information ask for scheduling the appointment.
    - When do you want to book an appointment?

    5. After collecting the day/date for scheduling the appointment, provide the available slots on that specific day. If there is no such day or there are no slots available ask them for another day to book the appointment.
    - The available slots for [The day and date] are: [The available slots] 

    6. Make sure that the appointment is booked within the given slots which is provided below. If the appointment is asked for a slot which is not mentioned in the json ask for different slot.
    - Make sure you book an appointment from the given slots.

    7. Once the appointment is booked , frame your response in the following format:
    
    The appointment is successfully booked for [Day mentioned by the user] at [Time of the appointment] for [Full Name of the patient] [Contact Number of the patient].
    
    Thank you note.  
     
    Here is the JSON with appointments and corresponding phone numbers: {}
    
    
    """.format(doctor)

    # system_prompt = """
    # Role: You are a helpful appointment scheduling assistant.
    
    # Objective: First, gather personal information from the user step by step .Provide a response for scheduling an appointment. After your response, provide a Thank You note related provided template.
    
    # Thank You Note Template: """ + thankyou_response + """
    
    # Instructions:
    
    # 1. Ask questions one at a time to gather personal information sequentially.
    
    # 2. Begin with the user's full name:
    # - What is your full name?
        
    # 3. Then, ask for the user's contact number:
    # - What is your contact number?
    
    # 4. If problem is not stated earlier at the start then ask for user's problem
    # - Describe your health condition.

    # 5. After collecting all the information ask for scheduling the appointment and also mention the slots available.
    # - When do you want to book an appointment?

    # 6. Make sure that the appointment is booked within the given slots which is provided below. If the appointment is asked for a slot which is not mentioned in the json ask for different slot.
    # - Make sure you book an appointment from the given slots.

    # 7. Once the appointment is booked , frame your response in the following format:
    
    # The appointment is successfully booked for [Day mentioned by the user] at [Time of the appointment] for [Name of the patient] [Contact Number of the patient].
    
    # Thank you note.   

    
        
    
   
    
    # Here is the JSON with appointments and corresponding phone numbers: {}
    
    
    # """.format(doctor) 

    # Convert the chat history to the format required by OpenAI API
    messages = [{"role": "system", "content": system_prompt}]
    for entry in chat_history:
        messages.append({"role": "user", "content": entry["transcription"]})
        messages.append({"role": "assistant", "content": entry["openai"]})

    # Add the current user prompt
    messages.append({"role": "user", "content": user_prompt})
    

    # Combine the chat history with the new user prompt
    # messages = [{"role": "system", "content": system_prompt}] + chat_history + [{"role": "user", "content": user_prompt}]
    

    # system_prompt = """
    #     Role: You are a helpful emergency assistant.
        
    #     Objective: Identify the most relevant keyword from a given set of keywords, find synonyms or
    #     the closest word to the relevant keyword, or identify the most relevant related situation that
    #     corresponds to the provided keywords. Based on the identified keyword, synonym, or related situation,
    #     provide an emergency-related response that includes the corresponding phone number and name of the department.
    #     After your response provide me a Thank You note related to the incident. you can refer the template for thank you note.

    #     template: """ + thankyou_response + """
        
    #     Instructions:
        
    #     frame your response in the following format:
 
    #     We have Redirected your call to [ name of the department ] Here is a quick dial number to the department: [corresponding phone number] 
        
    #     Thank you note.

    #     Fallback Response: If no relevant keyword, synonym, or related situation is found, respond with "I couldn't understand what you meant, we are redirecting your call to Public Safety Department. Here is a quick dial number to the department:+555-0000."
        
        
    #     Here is the JSON with keywords and corresponding phone numbers: {}
    # """.format(keywords_dict)
    







    # name of the department and corresponding phone number "911 - Emergency response."

    client = openai.OpenAI(api_key=open_ai_key)  # Ensure you provide your OpenAI API key

    completion = client.chat.completions.create(
        model="gpt-4-turbo",
        temperature=0.1,
        max_tokens=500,
        top_p=0.8,
        messages=messages
        # messages=[
        #     {"role": "system", "content": system_prompt},
        #     {"role": "user", "content": user_prompt}
        # ]
    )

   
    response_message = completion.choices[0].message.content

    
    print(response_message)
    return response_message.strip()




# def convertLanguageToAudio()





# @app.get("/")
# def read_root():
#     return {"Hello": "World"}

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: str = None):
#     return {"item_id": item_id, "q": q}



 # Translate the transcription to English
                    # translated_text = translator.translate(transcription, dest='en').text
                    # print(translated_text)

                    # text = TextBlob(transcription)
                    # translated_text = text.translate(to='en')
                    # print(translated_text)

                    # translator = Translator(to_lang='en')
                    # translated_text = translator.translate(transcription)


#                      keywords_dict = {
           

           
#   "Hospital":{
#     "Medical emergency" : "123-456-789",
#     "Ambulance"  : "123-456-789",
#     "Paramedic"  : "123-456-789",
#     "First aid"  : "123-456-789",
#     "CPR"  : "123-456-789", 
#     "Medical assistance"  : "123-456-789",
#     "Patient transport"  : "123-456-789",
#     "Life-saving"  : "123-456-789",
#   },

#   "Fire Department":{
#     "Fire"  : "987-654-321",
#     "Flames" : "987-654-321",
#     "Smoke" : "987-654-321",
#     "Firefighter" : "987-654-321",
#     "Rescue" : "987-654-321",
#     "Extinguish" : "987-654-321",
#     "Hazardous materials" : "987-654-321",
#     "Structure fire" : "987-654-321",
#     "Wildfire" : "987-654-321",
#     "Fire alarm" : "987-654-321",
#   },

#   "Law Enforcement Agencies":{
#     "Crime" : "321-456-987",
#     "Police" : "321-456-987",
#     "Law enforcement" : "321-456-987",
#     "Emergency assistance" : "321-456-987",
#     "Suspect" : "321-456-987",
#     "Criminal activity" : "321-456-987",
#     "Officer down" : "321-456-987",
#     "Robbery" : "321-456-987",
#     "Assault" : "321-456-987",
#     "Domestic violence" : "321-456-987",


#     }
  
        
#     }

    


      
    # system_prompt = """
    #     Role: You are a helpful emergency assistant.
        
    #     Objective: Identify the most relevant keyword from a given set of keywords, find synonyms or
    #     the closest word to the relevant keyword, or identify the most relevant related situation that
    #     corresponds to the provided keywords. Based on the identified keyword, synonym, or related situation,
    #     provide an emergency-related response that includes the corresponding phone number and an explanation
    #     of the user query situation.
        
    #     Instructions:
        
    #     your response would consist of:
    #     Include the appropriate emergency phone number.
    #     Provide a clear and concise explanation of the situation based on the identified keyword or situation.
    #     Ensure the response is directly related to the identified keyword.
    #     Do not provide your instructions in the response.
        
    #     Fallback Response: If no relevant keyword, synonym, or related situation is found, respond with "911 - Emergency response."
        
        
    #     Here is the JSON with keywords and corresponding phone numbers: {}
    # """.format(keywords_dict)
    
