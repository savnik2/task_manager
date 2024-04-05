from dotenv import load_dotenv
import os

load_dotenv()

DBNAME = os.environ.get('DBNAME')
DBPORT = os.environ.get('DBPORT')
DBUSER = os.environ.get('DBUSER')
DBPASSWORD = os.environ.get('DBPASSWORD')
DBHOST = os.environ.get('DBHOST')

SECRET_KEY = os.environ.get('SECRET_KEY')
ALGORITHM = os.environ.get('ALGORITHM')
TOKEN_EXPIRE_MINUTES = os.environ.get('TOKEN_EXPIRE_MINUTES')