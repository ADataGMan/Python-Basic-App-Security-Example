import os
import base64
from dotenv import load_dotenv

load_dotenv()

db_connection_params = {
    'host':os.getenv("DB_HOST"),
    'user':os.getenv("DB_USER_NAME"),
    'password':base64.b64decode(os.getenv("DB_USER_PASSWORD")).decode("utf-8"),
    'database':os.getenv("DB_NAME")
}

print(f'{db_connection_params["user"]} has connected to Database {db_connection_params["database"]} on {db_connection_params["host"]}')