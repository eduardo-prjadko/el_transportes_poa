from instances import get_session
from instances import get_env_var


URL = 'https://dadosabertos.poa.br'

def main(endpoint: str) -> dict:
    # instantiating request session 
    session = get_session()

    if endpoint == '':
        endpoint = '/api/3/action/datastore_search?resource_id=cb96a73e-e18b-4371-95c5-2cf20e359e6c'

    # get data
    r = session.get(f'{URL}{endpoint}')

    # if request fails, it raises an error
    if r.status_code != 200:
        raise Exception(f'data could not been downloaded. GET status code {r.status_code}')

    return r.json()
