import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

PORT = int(os.environ.get("PORT"))

DEBUG = os.environ.get("DEBUG") == "True"
