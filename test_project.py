from project import greet_game,select_mode,start_game
import pytest


def main():
    test_greet_game()
    test_select_mode()
    test_start_game()


def test_greet_game():
    assert greet_game() == True


def test_select_mode():
    mode = select_mode()
    assert mode in ['1', '2']


def test_start_game():
    with pytest.raises(SystemExit) as status:
        start_game("1")
    assert status.type == SystemExit
    assert status.value.code == "Game Ended!!!"

if __name__ == "__main__":
    main()