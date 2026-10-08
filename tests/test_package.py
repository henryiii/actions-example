import actions_example


def test_actions_example(capsys):
    actions_example.main()
    out, err = capsys.readouterr()
    assert "Hello" in out
