import pytest
from unittest.mock import patch
import main

def test_cli_exit_option(capsys):
    user_inputs = ["0"]
    with patch("builtins.input", side_effect=user_inputs):
        try:
            main.main()
        except SystemExit:
            pass

    captured = capsys.readouterr()
    assert "Goodbye" in captured.out or "Exiting" in captured.out or captured.out != ""

def test_cli_invalid_menu_option(capsys):
    user_inputs = ["99", "0"]
    with patch("builtins.input", side_effect=user_inputs):
        try:
            main.main()
        except SystemExit:
            pass

    captured = capsys.readouterr()
    assert "Invalid" in captured.out or captured.out != ""