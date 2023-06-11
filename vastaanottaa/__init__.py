"""Receive (Finnish: vastaanottaa) text traversing unknown territories."""
# [[[fill git_describe()]]]
__version__ = '2023.6.12+parent.v2023.6.11-8-g1f5b5866'
# [[[end]]] (checksum: d345d0da07a697d7034cb54e8b9b1e1f)
__version_info__ = tuple(
    e if '-' not in e else e.split('-')[0] for part in __version__.split('+') for e in part.split('.') if e != 'parent'
)

APP_NAME = 'Receive (Finnish: vastaanottaa) text traversing unknown territories.'
APP_ALIAS = 'vastaanottaa'
APP_ENV = APP_ALIAS.upper()
VERSION = __version__
VERSION_INFO = __version_info__

__all__ = [
    'APP_ALIAS',
    'APP_ENV',
    'APP_NAME',
    'VERSION',
    'VERSION_INFO',
]
