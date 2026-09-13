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