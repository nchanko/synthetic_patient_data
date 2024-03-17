from data_generation import generate_records,generate_patients
# Placeholder for any specific imports or code snippets that are relevant to orchestrating the workflow but not directly defined in the overview

# Main function definition

def main():
  #create patient names
  generate_patients(generate_time = 1, record_count =5, output_file_name ="patient_data.csv")
  #create patient's records
  generate_records(start_index=0,record_count=5, output_file_name="medical_data.csv")

main()
