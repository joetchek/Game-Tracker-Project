import os
from dotenv import load_dotenv

load_dotenv()

test = os.environ.get('TEST_VARIABLE')
print(test)