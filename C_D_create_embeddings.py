
from openai import OpenAI
from dotenv import load_dotenv
import os

# we could incorparate batch calling to facilitate parallel processing

def embed_caption_api(text_list, model="text-embedding-3-small"):
    
    ## access to API key
    notebook_directory = "C:/Users/Esra/Desktop/Deep_Learning/Image_Classification/Fashion/Classify_ThreadUp_Images"

    # Construct the absolute path to the api.env file
    env_file_path = os.path.join(notebook_directory, "api.env")

    # Load environment variables from the api.env file
    load_dotenv(env_file_path, override=True)

    # Access the API key
    api_key = os.getenv("OPENAI_API_KEY")

    os.environ['OPENAI_API_KEY'] = api_key

    client = OpenAI()

    # get embeddings in a batch 
    response = client.embeddings.create(input = text_list, model=model).data
    
    return [response[i].embedding for i in range(len(response))]






    
    