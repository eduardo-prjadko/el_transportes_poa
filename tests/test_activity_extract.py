import activity_extract


def test_activty_extract():
    r = activity_extract.main('')
    assert isinstance(r, dict)