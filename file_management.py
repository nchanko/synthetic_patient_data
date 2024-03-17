
from required_libaries import pd, time, os

# Function definitions related to saving and reading data
def check_csv(filename: str):
  """Check if the file exists"""
  try:
    with open(filename, 'r') as file:
        return True
  except FileNotFoundError:
      return False
  
def save_records(gen_recs: str,outputfilename:str):
  """Patient medical notes will be accepted"""
  #outputfilename ="medical_record2.csv"

  rec_values = gen_recs.split('|')
  medical_record = {
      'record_id': rec_values[0].split(":")[1].strip(),
      'date_of_visit': rec_values[1].split(":")[1].strip(),
      'patient_id': rec_values[2].split(":")[1].strip(),
      'patient_name': rec_values[3].split(":")[1].strip(),
      'age': (rec_values[4]).split(":")[1].strip(),
      'gender': rec_values[5].split(":")[1].strip(),
      'race': rec_values[6].split(":")[1].strip(),
      'country_of_origin': rec_values[7].split(":")[1].strip(),
      'chief_complaint': rec_values[8].split(":")[1].strip(),
      'history of present illness': rec_values[9].split(":")[1].strip(),
      'past medical and surgical history': rec_values[10].split(":")[1].strip(),
      'immunization history': rec_values[11].split(":")[1].strip(),
      'allergy history': rec_values[12].split(":")[1].strip(),
      'currently taking drugs': rec_values[13].split(":")[1].strip(),
      'social/personal history': rec_values[14].split(":")[1].strip(),
      'investigation records': rec_values[15].split(":")[1].strip(),
      'lab tests and results': rec_values[16].split(":")[1].strip(),
      'differential diagnosis': rec_values[17].split(":")[1].strip(),
      'treatment and management plan': rec_values[18].split(":")[1].strip(),
      'additional notes': rec_values[19].split(":")[1].strip()
  }

  # create a DataFrame from the medical record dictionary
  df = pd.DataFrame.from_dict([medical_record])

  # reorder the columns to match the desired order
  df = df[['record_id', 'date_of_visit', 'patient_id', 'patient_name', 'age', 'gender', 'race', 'country_of_origin', 'chief_complaint',
          'history of present illness', 'past medical and surgical history', 'immunization history', 'allergy history', 'currently taking drugs',
          'social/personal history', 'investigation records', 'lab tests and results', 'differential diagnosis', 'treatment and management plan',
          'additional notes']]

  # export the DataFrame to a CSV file
  df.to_csv(outputfilename, mode='a', header=False,index=False)
  print("Record saved successfully")

def save_patient(patient_names: str,outfile_name:str):
    """patient names, output file name.csv and source file name.csv will be accepted"""
    # Load the existing patient data
    #outfile_name = "patient_data.csv"
    if os.path.exists(outfile_name):
        # Load the existing patient data
        df = pd.read_csv(outfile_name,header = None)
        if df.empty:
            max_id = 0
        else:
            # Get the maximum ID value in the existing data
            max_id = df[0].str.replace('P', '').astype(int).max()
    else:
        # File doesn't exist, start max index from zero
        max_id = 0
    start_id = max_id+1

    records = patient_names.split('\n')

    # Create an empty list to store the patient data
    patient_data = []

    # Loop through each record and extract the patient information
    # Loop through each record and extract the patient information
    for record in records:
        # Skip empty records
        if not record:
            continue
        # Split the record into individual data fields
        try:
            record_data = record.split('|')
            # Extract the patient information from the record
            id = 'P' + str(start_id).zfill(6)
            name = record_data[0].split('. ')[1].strip()
            age = record_data[1].strip()
            gender = record_data[2].strip()
            race = record_data[3].strip()
            country = record_data[4].strip()
            chief_complaint = record_data[5].strip()
            disease = record_data[6].strip()
            # Add the patient data to the list
            patient_data.append([id, name, age, gender, race, country, chief_complaint, disease])
            # Increment the max_id variable
            start_id += 1
        except Exception as e:
            print("Error: ", e)
            print("Retrying after 1 seconds...")
            time.sleep(1)
            # Retry the same record after waiting for 5 seconds and start the id after the most recent id
            start_id = int(patient_data[-1][0].strip('P')) + 1 if patient_data else start_id
            continue

    # Convert the list of patient data to a DataFrame
    df = pd.DataFrame(patient_data, columns=['Patient ID', 'Name', 'Age', 'Gender', 'Race', 'Country of Origin', 'Chief Complaint', 'Disease'])
    # Append the data to the existing file
    print("pass")
    df.to_csv(outfile_name, mode='a', header=False, index=False)
    print(f"Successfully appended to file {outfile_name}")