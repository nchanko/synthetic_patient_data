# Medical Record Synthesis using GPT-3.5
### Author Dr.Nyein Chan Ko Ko (2023)

## Overview
This project leverages GPT-3.5 to synthesize medical records, aiming to provide a compliant solution for researchers needing access to patient data while respecting privacy laws like HIPAA and GDPR. 

## Repository Contents
- `main.py`: Main function execution
- `data_generation.py`: Synthetic patient profile and record generation
- `gpt_processing.py`: GPT model utilization for record creation
- `file_management.py`: Transformation of GPT texts into CSV
- `required_libraries.py`: Library imports

## Objectives
- Evaluate synthetic medical record generation feasibility and accuracy
- Process analysis from prompt engineering to database-ready notes
- Apply findings in language model research and prototyping

## Methodology
- **Prompt Engineering**: Develop prompts for GPT-3.5 to accurately generate medical data
- **Data Generation**: Create patient profiles and detailed medical records
- **Data Processing**: Convert generated texts to structured CSV format

## Observations
- Generated 1079 balanced patient records by nationality and gender
- Noted realistic age distributions and disease prevalences
- Addressed potential biases and the importance of reliable data sources

## Applications
- Enhancing NLP tasks in healthcare
- Supporting medical education and research
- Prototype testing within privacy regulations

## Conclusion
The project highlights the potential of GPT-3.5 in synthesizing realistic medical records, providing a valuable tool for medical research within ethical and legal standards.

## Usage
Install dependencies listed in `required_libraries.py`. Run `main.py` to begin synthetic medical record generation. Follow component-specific instructions for detailed operations.

Read more about this project [here](https://nyeimchankoko.medium.com/medical-record-synthesis-using-llm-a796d3c67fd0)
