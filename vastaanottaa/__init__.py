# [[[fill git_describe()]]]
__version__ = '2023.4.2+parent.2637a057'
# [[[end]]] (checksum: 203623ce1610b41c9139f2b591ffc9ff)
__version_info__ = tuple(
    e if '-' not in e else e.split('-')[0] for part in __version__.split('+') for e in part.split('.') if e != 'parent'
)
