import sys

import pytest

# XFAIL
# use when its expected that functions will fail


# expected to fail, if it would pass -> terminal = XPASS
@pytest.mark.xfail(reason="Expected to fail because XYY")
def test_str04():
    letters = "xihdjhfjhwkjdkwjdekfjfk"
    assert letters[5000] == "x"


# mark as fail when function not working on linux
@pytest.mark.xfail(sys.platform == "linux", reason="doesnt work on linux")
def test_str05():
    letters = "abcd"
    num = 1234
    result = letters + str(num)
    assert result == "abcd12345"
