from typing import List, Tuple


def struct(name: str, members: List[Tuple[str, ...]]) -> str:
    assert members, 'Not very useful without any members'

    text = """class %s:
    def __init__(self, """ % (name,)

    init_parameters = ', '.join('%s: %s' % m if len(m) == 2 else '%s: %s = %s' % m for m in members)
    text += init_parameters

    text += ') -> None:\n'

    for m in members:
        member_name = m[0]
        text += '        self.%s = %s\n' % (member_name, member_name)

    text += """
    def __repr__(self) -> str:
        fields = [
"""
    member_names = [m[0] for m in members]
    for m in member_names:
        text += '            (%r, self.%s),\n' % (m, m)

    text += """        ]
        return '%s(%%s)' %% (
            ', '.join('%%s=%%r' %% kv for kv in fields),
        )""" % (name,)

    return text
