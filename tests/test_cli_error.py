import pytest
import subprocess
from subprocess import PIPE


def test_pyencourage_call_exception():
    with pytest.raises(subprocess.CalledProcessError):
        subprocess.check_call('pyencouragement')


def test_pyencourage_call_output():
    try:
        p = subprocess.Popen('pyencouragement', stdin=PIPE, stdout=PIPE, stderr=PIPE)
    except:
        out, err = p.communicate()
        assert out == b'Did you mean pyencourage?'
        assert p.returncode == 1
        pass
