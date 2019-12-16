from unittest.mock import patch
from main import main_handler
import sys

@patch("main.hello_world")
def test_mock_external_incorrect(mock_hello_world):
    mock_hello_world.return_value = "Hello Dolly!"
    assert main_handler() == "Hello Dolly!"


for path in sys.path:
    print(path)