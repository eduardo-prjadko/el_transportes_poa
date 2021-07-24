import instances


def test_get_session():
    r = instances.get_session()
    assert r

def test_get_env_var():
    r = instances.get_env_var()
    assert r.URL

def test_get_storage_client():
    r = instances.get_storage_client()
    assert r