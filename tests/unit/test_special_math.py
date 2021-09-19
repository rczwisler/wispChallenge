import pytest
from wisp_api import create_app
from wisp_api import special_math

@pytest.fixture
def api():
    api = create_app()
    with api.test_client() as api:
        yield api

def test_special_math_memoize():
    result = special_math.special_math_memoize(7)
    assert result == 79

    result = special_math.special_math_memoize(17)
    assert result == 10926

def test_special_math_iterative():
    result = special_math.special_math_iterative(7)
    assert result == 79

    result = special_math.special_math_iterative(17)
    assert result == 10926

def test_special_math_endpoint(api):
    result = api.get('specialMath/7')
    assert result.data == b'79'

    result = api.get('specialMath/17')
    assert result.data == b'10926'

def test_value_error_input(api):
    result = api.get('specialMath/-1')
    assert b'Invalid input' in result.data

def test_type_error_input(api):
    result = api.get('specialMath/foo')
    assert b'Invalid input' in result.data

def test_90(api):
    result = api.get('specialMath/90')
    print(result.status)
    assert result.status == '200 OK'
