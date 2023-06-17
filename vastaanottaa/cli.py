"""Command line interface for vastaanottaa."""
# import argparse
import base64
import datetime as dti
import os
import pathlib
import sys
import time
from typing import no_type_check

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from vastaanottaa import APP_ALIAS, APP_ENV, VERSION

SEND = 'send'
RECV = 'recv'
ACTIONS = (SEND, RECV)
ENCODING = 'utf-8'
HASH_ALG = hashes.BLAKE2b
RES_KEY_LEN = 32
SALT_LEN = 16
SALT = os.urandom(SALT_LEN)
N_ITER = 480000

ARMOR_MSG_BEGIN = f'---- BEGIN {APP_ENV} MESSAGE ----'
ARMOR_MSG_END = f'---- END {APP_ENV} MESSAGE ----'

ARMOR_MSG_BEGIN_BYTES = ARMOR_MSG_BEGIN.encode(ENCODING)
ARMOR_MSG_END_BYTES = ARMOR_MSG_BEGIN.encode(ENCODING)

ARMOR_PADDED_LENGTH = len(ARMOR_MSG_BEGIN_BYTES) + 1 + len(ARMOR_MSG_END_BYTES) + 1

ARMOR_SALT_BEGIN = f'---- BEGIN {APP_ENV} SALT ----'
ARMOR_SALT_END = f'---- END {APP_ENV} SALT ----'

USAGE_INFO = f'usage: {APP_ALIAS} send|recv given text-or-file salt-for-recv'


@no_type_check
def app(argv=None) -> int:
    """Do the thing."""
    argv = sys.argv[1:] if argv is None else argv

    if len(argv) == 1 and argv[0] in ('-V', '--version', 'version'):
        print(f'{APP_ALIAS} v{VERSION}', file=sys.stderr)
        return 0

    if not argv or len(argv) == 1 and argv[0] in ('-h', '--help', 'help'):
        print(USAGE_INFO, file=sys.stderr)
        return 0

    if len(argv) not in (3, 4):
        print('ERROR: unexpected count of parameters', file=sys.stderr)
        print(USAGE_INFO, file=sys.stderr)
        return 2
    action = argv[0].lower().strip()
    if action not in ACTIONS:
        print('ERROR: unexpected goal/action - use either send or recv', file=sys.stderr)
        print(USAGE_INFO, file=sys.stderr)
        return 2
    given = argv[1].encode(ENCODING)
    src = argv[2]

    salt = SALT
    if action == SEND and len(argv) == 4:
        print('WARNING: salt provided as parameter for send', file=sys.stderr)
        salt = base64.decodebytes(argv[3].encode(ENCODING))
    if action == RECV:
        if len(argv) != 4:
            print('ERROR: salt missing for recv', file=sys.stderr)
            print(USAGE_INFO, file=sys.stderr)
            return 2
        salt = base64.decodebytes(argv[3].encode(ENCODING))

    src_path = pathlib.Path(src)
    if src_path.is_file():
        print('INFO: Reading content from file', file=sys.stderr)
        src_data = src_path.open('rb').read()
    else:
        print('INFO: Loading content from parameter', file=sys.stderr)
        src_data = src.encode(ENCODING)

    if not src_data:
        print('ERROR: afraid of the void - content for message has zero bytes', file=sys.stderr)
        print(USAGE_INFO, file=sys.stderr)
        return 1

    kdf = PBKDF2HMAC(
        algorithm=HASH_ALG(64),
        length=RES_KEY_LEN,
        salt=salt,
        iterations=N_ITER,
    )
    key = base64.urlsafe_b64encode(kdf.derive(given))
    f = Fernet(key)
    ts = int(time.time())
    ts_dt = dti.datetime.fromtimestamp(ts, dti.timezone.utc)

    if action == SEND:
        token = f.encrypt_at_time(src_data, ts)
        control_ts = f.extract_timestamp(token)
        control_ts_dt = dti.datetime.fromtimestamp(control_ts, dti.timezone.utc)
        print(f'DEBUG: timestamp embedded:  {control_ts} ({ts_dt})', file=sys.stderr)
        print(f'DEBUG: timestamp extracted: {ts} ({control_ts_dt})', file=sys.stderr)
        trp = base64.encodebytes(token)
        print(ARMOR_MSG_BEGIN)
        print(trp.decode(ENCODING), end='')
        print(ARMOR_MSG_END)
        print(file=sys.stderr)
        print(ARMOR_SALT_BEGIN, file=sys.stderr)
        print(base64.encodebytes(salt), file=sys.stderr)
        print(ARMOR_SALT_END, file=sys.stderr)
        return 0

    if src_data.startswith(ARMOR_MSG_BEGIN_BYTES) and len(src_data) > ARMOR_PADDED_LENGTH:
        src_data = src_data[len(ARMOR_MSG_BEGIN_BYTES) + 1 : -len(ARMOR_MSG_END_BYTES) + 1]

    rcv = base64.decodebytes(src_data)
    print(f.decrypt(rcv).decode(ENCODING))

    return 0
