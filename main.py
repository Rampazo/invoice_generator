import os
import starkbank
from dotenv import load_dotenv
from cronjob import start_cronjob

load_dotenv()

starkbank.user = starkbank.Project(
    environment=os.getenv("STARKBANK_ENVIROMENT"),
    id=os.getenv("STARKBANK_PROJECT_ID"),
    private_key=os.getenv("STARKBANK_PRIVATE_KEY")
)

if __name__ == "__main__":
    start_cronjob()