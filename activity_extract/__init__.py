import logging

from instances import get_session
from instances import get_env_var


def main(name: str) -> dict:
    # instantianting request session 
    session = get_session()

    # instantianting environment variables
    env = get_env_var()

    # get data
    r = session.get(env.URL)

    return r.json()