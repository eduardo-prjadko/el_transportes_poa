import os
from string import Template

from azure.storage.blob import BlobServiceClient
import requests


# respective instances returned by functions below
session = None
env = None
storage_client = None

# class for environment variables
class EnvVar:
    HOST = 'https://dadosabertos.poa.br'
    ENDPOINT= Template('/api/3/action/datastore_search?limit=$limit&offset=$offset&resource_id=cb96a73e-e18b-4371-95c5-2cf20e359e6c')
    CONTAINER = None
    LIMIT = None

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
        env.CONTAINER = os.environ.get('CONTAINER')
        env.LIMIT = os.environ.get('LIMIT')
    
    return env

def get_storage_client():
    global storage_client
    if not storage_client:
        conn_string = os.environ.get('AzureWebJobsStorage')
        storage_client = BlobServiceClient.from_connection_string(conn_string)
    
    return storage_client