from jamaibase import JamAI, protocol as p
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

api_key = os.getenv("API_KEY")
project_id = os.getenv("PROJECT_ID")

jamai = JamAI(api_key=api_key, project_id=project_id)
