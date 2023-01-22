from incolumepy.barcode import __version__
import re
import pytest


@pytest.mark.parametrize(
    'entrance expected'.split(),
    (
        ('0.1.0', True),
        ('10.11.10', True),
        ('1.11.10-alpha.999', True),
        ('1.1.1-a.9', True),
        ('1.1.1a9', True),
    )
)
def test_version(entrance, expected):
    assert bool(re.fullmatch(r'(\d+\.){2}\d+(-?\w+\.?\d+)?', entrance, flags=re.I)) == expected
