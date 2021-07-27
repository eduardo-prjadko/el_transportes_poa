import activity_extract
from instances import get_env_var


def test_activty_extract():
    env = get_env_var()
    host = env.HOST
    limit = env.LIMIT
    endpoint = env.ENDPOINT.substitute(limit=limit, offset=0)
    r = activity_extract.main(f'{host}{endpoint}')
    assert isinstance(r, dict)