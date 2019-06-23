import pytest

from .abbreviator import Abbreviator


class TestAbbreviator:

    @pytest.mark.parametrize("inp, target, expected", [
        ("small diagonal cross", 12, "sma diag cro"),
        ("small diagonal cross", 11, "sma dia cro"),
        ("small diagonal cross", 10, "sm dia cro"),
        ("small diagonal cross", 9, "sm dia cr"),
        ("small diagonal cross", 8, "sm di cr"),
    ])
    def test_abbreviate_returns_target_length_strings_given_string_input(self, inp, target, expected):
        sut = Abbreviator(target_length=target)
        res = sut.abbreviate(inp)
        assert expected == res

    @pytest.mark.parametrize("inp, target, expected", [
        ("small diagonal cross", 5, "s d c"),
        ("small diagonal cross", 1, "s d c"),
    ])
    def test_abbreviate_returns_min_each_word_length_1_given_smaller_than_possible_target(self, inp, target, expected):
        sut = Abbreviator(target_length=target)
        res = sut.abbreviate(inp)
        assert expected == res

    @pytest.mark.parametrize("inp, target, expected", [
        ("fantastic", 5, "fanta"),
        ("fantastic", 8, "fantasti"),
        ("fantastic", 8, "fantasti"),
    ])
    def test_abbreviate_abbreviates_given_single_word(self, inp, target, expected):
        sut = Abbreviator(target_length=target)
        res = sut.abbreviate(inp)
        assert expected == res

    @pytest.mark.parametrize("inp, target, expected", [
        ("", 1986, ""),
        ("", 1, ""),
    ])
    def test_abbreviate_returns_empty_string_given_empty_string(self, inp, target, expected):
        sut = Abbreviator(target_length=target)
        res = sut.abbreviate(inp)
        assert expected == res

    @pytest.mark.parametrize("target_length", [
        0, -1
    ])
    def test_new_instance_raises_value_error_given_non_positive_target(self, target_length):
        with pytest.raises(ValueError, match='target_length must be greater than 0.'):
            Abbreviator(target_length=-1)
