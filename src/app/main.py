from flask import Flask
from dotenv import load_dotenv
import os

app = Flask(__name__)

# If Debug is set to True, indicating development mode, otherwise, it implies production mode.
app.config['DEBUG'] = True

# "app.debug" determines whether the application's debug mode is enabled or disabled.
if app.debug:
    # loading dev environment file
    load_dotenv("src/utils/environments/.env.dev")
else:
    # loading prod environment file
    load_dotenv("src/utils/environments/.env.prod")

@app.route("/")
def hello_world():
    # Retrieve the connection string from the environment file
    Db_Connection_String = os.getenv("DATABASE_CONNECTION_STRING", default="Uh-oh! Looks like we're missing an environment variable!")
    return f"{Db_Connection_String}"

if __name__ == "__main__":
    app.run(port=8000)