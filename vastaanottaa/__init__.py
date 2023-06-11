"""Receive (Finnish: vastaanottaa) text traversing unknown territories."""
# [[[fill git_describe()]]]
__version__ = '2023.6.12+parent.gf1b5cf69'
# [[[end]]] (checksum: c65b3f25c3013583a659479eccace65b)
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
