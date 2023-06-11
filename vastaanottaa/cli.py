"""Command line interface for vastaanottaa."""
# import argparse
import base64
import os
import pathlib
import sys
import time
from typing import no_type_check

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

SEND = 'send'
RECV = 'recv'
ACTIONS = (SEND, RECV)
ENCODING = 'utf-8'
HASH_ALG = hashes.BLAKE2b
RES_KEY_LEN = 32
SALT_LEN = 16
SALT = os.urandom(SALT_LEN)
N_ITER = 480000


@no_type_check
def app(argv=None) -> int:
    """Do the thing."""
    argv = sys.argv[1:] if argv is None else argv
    if len(argv) not in (3, 4):
        print('The count!')
        return 2
    action = argv[0].lower().strip()
    if action not in ACTIONS:
        print('The goal?')
        return 2
    given = argv[1].encode(ENCODING)
    src = argv[2]

    salt = SALT
    if len(argv) == 4:
        print('A test, right?')
        salt = base64.decodebytes(argv[3].encode(ENCODING))
    if action == RECV:
        if len(argv) != 4:
            print('The salt!')
            return 2
        salt = base64.decodebytes(argv[3].encode(ENCODING))

    src_path = pathlib.Path(src)
    if src_path.is_file():
        print('Reading file ...')
        src_data = src_path.open('rb').read()
    else:
        print('Name is content ...')
        src_data = src.encode(ENCODING)

    if not src_data:
        print('Afraid of the void!')
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

    if action == SEND:
        token = f.encrypt_at_time(src_data, ts)
        control_ts = f.extract_timestamp(token)
        print(f'sender: {control_ts=} with {ts=}')
        trp = base64.encodebytes(token)
        print('encoded:')
        print(trp.decode(ENCODING))
        rcv = base64.decodebytes(trp)
        print(f'receiver: {f.extract_timestamp(rcv)=} with {ts=}')
        print('data:')
        print(f.decrypt(rcv).decode(ENCODING))
        print('# --- 8< ---')
        print(f'- no pepper but {base64.encodebytes(salt)=}')
        return 0

    rcv = base64.decodebytes(src_data)
    print(f'receiver: {f.extract_timestamp(rcv)=} with {ts=}')
    print(f'- using {base64.encodebytes(salt)=}')
    print('data:')
    print(f.decrypt(rcv).decode(ENCODING))

    return 0
