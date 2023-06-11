# [[[fill git_describe()]]]
__version__ = '2023.6.11+parent.nonce-14-g01364449'
# [[[end]]] (checksum: 13c6a6e4ff55f130ac3378cd84eeccef)
__version_info__ = tuple(
    e if '-' not in e else e.split('-')[0] for part in __version__.split('+') for e in part.split('.') if e != 'parent'
)
