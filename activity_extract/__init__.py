from instances import get_session
from instances import get_env_var


def main(name: str) -> dict:
    # instantianting request session 
    session = get_session()

    # instantianting environment variables
    env = get_env_var()

    # get data
    r = session.get(env.URL)

    # if request fails, it raises en error
    if r.status_code != 200:
        raise Exception(f'data could not been downloaded. GET status code {r.status_code}')

    return r.json()