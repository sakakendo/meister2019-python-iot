from src.kadai1.main import hello


def test_kadai1(capsys):
    hello()
    captured = capsys.readouterr()
    assert captured.out == "hello world\n"
