import pandas
import os

# new for .env example
from dotenv import load_dotenv

load_dotenv()

print ("Hello Demo")

key =True if os.getenv('API_KEY') else False
print (f"API_KEY exists: {key}")