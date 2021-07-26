import os

from azure.storage.blob import BlobServiceClient
import requests


# respective instances returned by functions below
session = None
env = None
storage_client = None

# class for environment variables
class EnvVar:
    URL = None
    CONTAINER = None

def get_session():
    global session
    if not session:
        headers = {
            'Accept': 'aplication/json',
            'Content-Type': 'application/json'
        }
        session = requests.Session()
        session.headers.update(headers)
    
    return session

def get_env_var():
    global env
    if not env:
        env = EnvVar()
        env.URL = os.environ.get('URL')
        env.CONTAINER = os.environ.get('CONTAINER')
    
    return env

def get_storage_client():
    global storage_client
    if not storage_client:
        conn_string = os.environ.get('AzureWebJobsStorage')
        storage_client = BlobServiceClient.from_connection_string(conn_string)
    
    return storage_client