from instances import get_session


def main(url: str) -> dict:
    # instantiating request session 
    session = get_session()

    # get data
    r = session.get(url)

    # if request fails, it raises an error
    if r.status_code != 200:
        raise Exception(f'data could not been downloaded. GET status code {r.status_code}')

    return r.json()
