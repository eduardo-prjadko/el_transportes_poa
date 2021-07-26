from datetime import datetime
import json

from azure.core.exceptions import ResourceNotFoundError

from instances import get_storage_client


def main(uploadopt: dict) -> str:
    
    # params
    container = uploadopt['container']
    data = uploadopt['data']
    index = uploadopt['index']

    # instantiates storage client
    storage_client = get_storage_client()

    # creates a conteiner if it doesn't exists 
    try:
        conteiner_client = storage_client.get_container_client(container=container)
        conteiner_client.get_container_properties()
    except ResourceNotFoundError:
        conteiner_client = storage_client.create_container(container)
    
    # creates blob
    today = datetime.today().date()
    path = f'{today.year}/{today.month}/{today.day}'
    blob_name = f'{path}/{today.year}{today.month}{today.day}_transportepoa_{index}.json'
    json_data = json.dumps(data)
    blob = conteiner_client.upload_blob(name=blob_name, data=json_data, overwrite=True)

    return 'succeed'