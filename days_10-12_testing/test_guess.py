from unittest.mock import patch
import random
from guess import get_random_number, Game
import black

# Every time random is called should return 17 with this patch mock
@patch.object(random, "randint")
def test_get_random_number(m):
    m.return_value = 17
    assert get_random_number() == 17


# @patch("builtins.input", side_effects=[11, "12", "bob", 12, 5, -1, 21, 7, None])
# def test_guess():
#     game = Game()
#     game()
