import pytest

from credmgr.models.utils import CachedProperty


@pytest.yield_fixture()
def credentialManager():
    yield None


@pytest.yield_fixture(autouse=True)
def recorder(credentialManager):
    yield None


class ClassPropertyTest:
    @CachedProperty
    def nine(self):
        """Return 9."""
        return 9

    def ten(self):
        return 10

    @property
    def eleven(self):
        return 11

    ten = CachedProperty(ten, doc="Return 10.")


def testCachedPropertyGet():
    cachedPropertyClass = ClassPropertyTest()
    assert "nine" not in cachedPropertyClass.__dict__
    assert cachedPropertyClass.nine == 9
    assert "nine" in cachedPropertyClass.__dict__
    assert "ten" not in cachedPropertyClass.__dict__
    assert cachedPropertyClass.ten == 10
    assert "ten" in cachedPropertyClass.__dict__
    assert "eleven" not in cachedPropertyClass.__dict__
    assert cachedPropertyClass.eleven == 11
    assert "eleven" not in cachedPropertyClass.__dict__


def testCachedPropertyDoc():
    assert ClassPropertyTest.nine.__doc__ == "Return 9."
    assert ClassPropertyTest.ten.__doc__ == "Return 10."
