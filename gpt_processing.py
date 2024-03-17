
from required_libaries import client

# Placeholder for any specific imports or functions that are relevant to GPT processing but not directly defined in the overview

# Function definitions related to processing or generating text with GPT models

def process_gpt(user_request : str, record_count: int = 10 ,prompt_num: int = None ):
  """user_request is the prompt from user.
  prompt_num is the option to select system prompt,
  1 to generate patient names.
  2 to generate patient medical record."""


  if prompt_num == 1:
    system_prompt = str(f"""Generate {record_count} dummy patient records.
    I will provide the list of differential diseases and country of origin.
    You will answer me with full names, ages, genders, race, country of origin , chief complaint(reason to visit the doctor) ,disease.
    Your chief complaint must be complex with overlap symptoms and should be relevant to the country of origin. Separate each line by \n and separate each cell by |.
    Do not write extra sentences. Do not index.Example format: 1. Sarah Fish |23|Female| White| USA| Fever, headache, joint pains, and vomiting|disease. My first request is
    .""")
  elif prompt_num ==2:
    system_prompt =str(f"""Generate {record_count} medical note for the given patient .I will provide you the patient_id,name,age,gender,race, country of origin and chief complaint. You will answer me these columns:
   record_id (format : ddmmpatient_id)| date_of_visit(dd/mm/yyyy) |patient_id |patient_name |age|gender|race|country_of_origin| chief_complaint| history_of_present_illness| past_medical_and_surgical_history|immunization_history |allergy_history| currently_taking_drugs |social_personal_history |investigation_records| lab_tests_and_results| differential_diagnosis| treatment_and_management_plan| additional_notes. Each column must be separated by "|".
   Each entry must be similar to a natural medical note can user + or - for present and absent. currently taking drugs must include name,dosage,form,frequency and duration.
   Do not write extra sentences.
   If more information is required to add , put in additional notes. If there is nothing to generate ,write Null.
   The medical note must be as complete as possible and must be relevant to chief complaint. History must contain all relevant additional information related to patient chief complaint.
   Example format is Example format: 'record_id: date_of_visit+patient_id'|'date_of_visit: dd/mm/yyyy'| 'patient_id: P000003'| 'patient_name: Aung Soe'| 'age: 55'|'gender: Male'| 'race: Asian'| 'country_of_origin: Myanmar'|'chief_complaint: Extreme thirst, frequent urination, numbness or tingling of feet.'|'history_of_present_illness: explain here'|'past_medical_and_surgical_history: explain here'| 'immunization_history: explain here'| 'allergy_history: explain here'| 'currently_taking_drugs: '| 'social_personal_history: explain here'| 'investigation_records: explain here'| 'lab_tests_and_results: explain here', 'differential_diagnosis: explain here' , 'treatment_and_management_plan: explain here', 'additional_notes: explain here.'
My first request is

    """)
  elif prompt_num ==3:
    system_prompt=""

  else:
    print("No prompt found")

  # Generate patient information using OpenAI API
  messages = [{"role": "system", "content":system_prompt },
          {"role": "user", "content": user_request}]


  model = "gpt-3.5-turbo"
  response = client.chat.completions.create(model=model, messages=messages, max_tokens=2000)
  generations = response.choices[0].message.content

  return generations



