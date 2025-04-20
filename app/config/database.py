import motor.motor_asyncio
import os



MONGO_URL = "mongodb+srv://akhilbsccs:akhilbsccs@cgac.dcxy29f.mongodb.net/?retryWrites=true&w=majority&appName=cgac"


client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URL)
db = client["cgac"]


# MONGO_URL = os.getenv("MONGO_URL")
# DB_NAME = os.getenv("DB_NAME")

# from dotenv import load_dotenv

# load_dotenv(override=True)
