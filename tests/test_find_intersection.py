import pytest
from easy.find_intersection import FindIntersection


@pytest.mark.parametrize("input_data, expected_output", [
  (["1, 3, 4, 7, 15", "3, 7, 9, 15"], "3,7,15"),
  (["1, 2, 3", "4, 5, 6"], "false"),
  (["7, 8, 9", "9, 10, 11"], "9"),
  (["22, 24, 25", "25, 26, 27, 28"], "25"),
])
def test_FindIntersection(input_data, expected_output, monkeypatch):
  monkeypatch.setattr('builtins.input', lambda: input_data)
  assert FindIntersection(input()) == expected_output
