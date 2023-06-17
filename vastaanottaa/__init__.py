"""Receive (Finnish: vastaanottaa) text traversing unknown territories."""
# [[[fill git_describe()]]]
__version__ = '2023.6.17+parent.g290b9c34'
# [[[end]]] (checksum: f906d477470ad7cc9067b497c89ebd43)
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
