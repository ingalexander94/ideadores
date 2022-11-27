import os
from dotenv import load_dotenv

load_dotenv()
PORT = os.getenv("PORT")
UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER")