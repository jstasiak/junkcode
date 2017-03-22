from cogmodules import struct


def test_struct():
    expected = """class Vector3f:
    def __init__(self, x: float, y: float, z: float = 0.0) -> None:
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self) -> str:
        fields = [
            ('x', self.x),
            ('y', self.y),
            ('z', self.z),
        ]
        return 'Vector3f(%s)' % (
            ', '.join('%s=%r' % kv for kv in fields),
        )"""
    assert struct('Vector3f', [('x', 'float'), ('y', 'float'), ('z', 'float', '0.0')]) == expected
