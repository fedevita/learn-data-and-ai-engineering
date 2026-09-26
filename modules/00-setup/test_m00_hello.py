from hello import greet


def test_greet_builds_the_greeting():
    assert greet("Federico") == "Ciao, Federico!"


def test_greet_works_with_any_name():
    assert greet("Anna") == "Ciao, Anna!"
