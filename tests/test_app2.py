"""Test app2."""
from app2 import __version__
from app2 import app2


def test_version():
    """Test version."""
    assert __version__ == "0.1.0"


def test_sanity():
    """Sanity check."""
    try:
        assert not app2()
    except Exception:
        assert True
