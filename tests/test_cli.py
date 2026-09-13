import pytest
from unittest.mock import patch
import main

def test_cli_exit_option(capsys):
    user_inputs = ["0"]