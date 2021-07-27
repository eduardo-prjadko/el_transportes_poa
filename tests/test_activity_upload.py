from azure.storage.blob import BlobClient
import pytest

import activity_upload


@pytest.fixture
def dumb_data():
    return {'testing': 'data'}

def test_activity_upload(dumb_data):
    parms = {
        'container': 'testcontainer',
        'data': dumb_data,
        'index': 0
    }
    r = activity_upload.main(parms)
    assert r == 'succeed'