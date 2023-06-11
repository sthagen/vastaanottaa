import vastaanottaa.cli as cli

SRC = 'README.mdxxxyyy'
SEC = 'Wie schön.'
SLT = 'n6ihE3dSantzwRwbs/prKw==\n'
TRG = '''\
Z0FBQUFBQmtoZERaTHN6Yk8tcnhRVFZfYzhPRnJMLWR2Q2Fnb2lRRGk4b0FxdkUyYWh3T3lUcm80
TFloYTEyTmdfbWJMQXhjblpkX3VSZmxDQ0xRcm5FSEJvZHlzWlNfYXc9PQ==
'''


def test_cli_send_uc_1(capsys):
    rc = cli.app(['send', SEC, SRC, SLT])
    assert rc == 0
    out, err = capsys.readouterr()
    assert 'test' in out
    assert not err


def test_cli_recv_uc_1(capsys):
    rc = cli.app(['recv', SEC, TRG, SLT])
    assert rc == 0
    out, err = capsys.readouterr()
    assert SLT.split('==', 1)[0] + '==' in out
    assert SRC in out
    assert not err


def test_cli_ac_short_0(capsys):
    rc = cli.app([])
    assert rc == 2
    out, err = capsys.readouterr()
    assert 'count' in out
    assert not err


def test_cli_ac_short_1(capsys):
    rc = cli.app(['send'])
    assert rc == 2
    out, err = capsys.readouterr()
    assert 'count' in out
    assert not err


def test_cli_ac_short_2(capsys):
    rc = cli.app(['send', SEC])
    assert rc == 2
    out, err = capsys.readouterr()
    assert 'count' in out
    assert not err


def test_cli_ac_short_5(capsys):
    rc = cli.app(['send', SEC, 'and', 'wun', 'off'])
    assert rc == 2
    out, err = capsys.readouterr()
    assert 'count' in out
    assert not err


def test_cli_ab_action(capsys):
    rc = cli.app(['unknown', SEC, SRC, SLT])
    assert rc == 2
    out, err = capsys.readouterr()
    assert 'goal' in out
    assert not err


def test_cli_ab_recv_no_salt(capsys):
    rc = cli.app(['recv', SEC, TRG])
    assert rc == 2
    out, err = capsys.readouterr()
    assert 'salt' in out
    assert not err


def test_cli_ab_data_zero_bytes(capsys):
    empty_source = 'test/fixtures/basic/empty.src'
    rc = cli.app(['send', SEC, empty_source])
    assert rc == 1
    out, err = capsys.readouterr()
    assert 'test' not in out
    assert 'void' in out
    assert not err
