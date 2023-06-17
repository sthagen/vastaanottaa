import vastaanottaa.cli as cli
from vastaanottaa import APP_ALIAS, VERSION

SRC = 'README.mdxxxyyy'
SEC = 'Wie schön.'
SLT = 'n6ihE3dSantzwRwbs/prKw==\n'
TRG = """\
Z0FBQUFBQmtoZERaTHN6Yk8tcnhRVFZfYzhPRnJMLWR2Q2Fnb2lRRGk4b0FxdkUyYWh3T3lUcm80
TFloYTEyTmdfbWJMQXhjblpkX3VSZmxDQ0xRcm5FSEJvZHlzWlNfYXc9PQ==
"""

SLT_NULL = ''

SRC_ARMOR_A_1 = 'test/fixtures/basic/armored.vastaanottaa'
SRC_RAW_A_1 = 'test/fixtures/basic/armored.vastaanottaa.raw'
SEC_A_1 = 'ja'
SLT_A_1 = '213gJL0ib2LC++IyWx97VA==\n'


def test_cli_send_uc_1(capsys):
    rc = cli.app(['send', SEC, SRC, SLT])
    assert rc == 0
    out, err = capsys.readouterr()
    assert 'salt provided as parameter' in err
    assert 'MESSAGE' in out


def test_cli_recv_uc_1(capsys):
    rc = cli.app(['recv', SEC, TRG, SLT])
    assert rc == 0
    out, err = capsys.readouterr()
    assert 'content' in err
    assert SRC in out


def test_cli_recv_uc_armor_a_1(capsys):
    rc = cli.app(['recv', SEC_A_1, SRC_ARMOR_A_1, SLT_A_1])
    assert rc == 0
    out, err = capsys.readouterr()
    assert 'content' in err
    assert 'nein' in out


def test_cli_recv_uc_raw_a_1(capsys):
    rc = cli.app(['recv', SEC_A_1, SRC_RAW_A_1, SLT_A_1])
    assert rc == 0
    out, err = capsys.readouterr()
    assert 'content' in err
    assert 'nein' in out


def test_cli_uc_version_1(capsys):
    for arg in ('-V', '--version', 'version'):
        rc = cli.app([arg])
        assert rc == 0
        out, err = capsys.readouterr()
        assert APP_ALIAS in err
        assert VERSION in err
        assert not out


def test_cli_uc_help_1(capsys):
    for arg in ('-h', '--help', 'help'):
        rc = cli.app([arg])
        assert rc == 0
        out, err = capsys.readouterr()
        assert 'usage: ' in err


def test_cli_uc_short_0(capsys):
    rc = cli.app([])
    assert rc == 0
    out, err = capsys.readouterr()
    assert 'usage: ' in err
    assert not out


def test_cli_ac_short_1(capsys):
    rc = cli.app(['send'])
    assert rc == 2
    out, err = capsys.readouterr()
    assert 'count' in err
    assert not out


def test_cli_ac_short_2(capsys):
    rc = cli.app(['send', SEC])
    assert rc == 2
    out, err = capsys.readouterr()
    assert 'count' in err
    assert not out


def test_cli_ac_short_5(capsys):
    rc = cli.app(['send', SEC, 'and', 'wun', 'off'])
    assert rc == 2
    out, err = capsys.readouterr()
    assert 'count' in err
    assert not out


def test_cli_ab_action(capsys):
    rc = cli.app(['unknown', SEC, SRC, SLT])
    assert rc == 2
    out, err = capsys.readouterr()
    assert 'goal' in err
    assert not out


def test_cli_ab_recv_no_salt(capsys):
    rc = cli.app(['recv', SEC, TRG])
    assert rc == 2
    out, err = capsys.readouterr()
    assert 'salt' in err
    assert not out


def test_cli_ab_data_zero_bytes(capsys):
    empty_source = 'test/fixtures/basic/empty.src'
    rc = cli.app(['send', SEC, empty_source])
    assert rc == 1
    out, err = capsys.readouterr()
    assert 'provided' not in err
    assert 'void' in err
    assert not out
