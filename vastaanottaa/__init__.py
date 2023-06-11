"""Receive (Finnish: vastaanottaa) text traversing unknown territories."""
# [[[fill git_describe()]]]
__version__ = '2023.6.11+parent.nonce-22-gf6f6ee63'
# [[[end]]] (checksum: 0f8e8f8d7b81c378f121b5bad0131c4b)
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
