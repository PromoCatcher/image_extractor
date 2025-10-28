from os import environ

from dotenv import load_dotenv


load_dotenv()


SA_KEY_PATH = environ["SA_KEY_PATH"]
BUCKET_NAME = environ["BUCKET_NAME"]
