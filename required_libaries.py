from openai import OpenAI
from tqdm import tqdm
import time
import pandas as pd
import os
import csv
from dotenv import load_dotenv
load_dotenv()


openaikey = os.getenv("OPENAI_KEY") 
client = OpenAI(api_key=openaikey)