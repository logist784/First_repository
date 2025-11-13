import pytest
from string_utils import StringUtils

string_utils = StringUtils()


class TestCapitalize:
    @pytest.mark.positive
    @pytest.mark.parametrize(
        "input_str, expected",
        [
            ("skypro", "Skypro"),
            ("hello world", "Hello world"),
            ("python", "Python"),
            ("тест", "Тест"),
            ("123abc", "123abc"),
            ("04 апреля 2023", "04 апреля 2023"),
        ],
    )
    def test_capitalize_positive(self, input_str, expected):
        assert string_utils.capitalize(input_str) == expected

    @pytest.mark.negative
    @pytest.mark.parametrize(
        "input_str, expected",
        [
            ("", ""),
            ("   ", "   "),
            ("123", "123"),
        ],
    )
    def test_capitalize_negative(self, input_str, expected):
        assert string_utils.capitalize(input_str) == expected


class TestTrim:
    @pytest.mark.positive
    @pytest.mark.parametrize(
        "input_str, expected",
        [
            ("   skypro", "skypro"),
            ("  hello world", "hello world"),
            ("   python", "python"),
            ("   тест", "тест"),
            ("   04 апреля 2023", "04 апреля 2023"),
            ("  123", "123"),
        ],
    )
    def test_trim_positive(self, input_str, expected):
        assert string_utils.trim(input_str) == expected

    @pytest.mark.negative
    @pytest.mark.parametrize(
        "input_str, expected",
        [
            ("", ""),
            ("test", "test"),
            ("test   ", "test   "),
            ("123", "123"),
        ],
    )
    def test_trim_negative(self, input_str, expected):
        assert string_utils.trim(input_str) == expected


class TestContains:
    @pytest.mark.positive
    @pytest.mark.parametrize(
        "string, symbol, expected",
        [
            ("SkyPro", "S", True),
            ("SkyPro", "k", True),
            ("SkyPro", "P", True),
            ("hello world", " ", True),
            ("04 апреля 2023", "а", True),
            ("12345", "3", True),
            ("тест", "т", True),
        ],
    )
    def test_contains_positive_true(self, string, symbol, expected):
        assert string_utils.contains(string, symbol) == expected

    @pytest.mark.positive
    @pytest.mark.parametrize(
        "string, symbol, expected",
        [
            ("SkyPro", "U", False),
            ("hello", "x", False),
            ("12345", "6", False),
            ("тест", "ы", False),
        ],
    )
    def test_contains_positive_false(self, string, symbol, expected):
        assert string_utils.contains(string, symbol) == expected

    @pytest.mark.negative
    @pytest.mark.parametrize(
        "string, symbol, expected",
        [
            ("", "a", False),
            ("   ", "a", False),
            ("test", "", False),
            ("", "", False),
        ],
    )
    def test_contains_negative(self, string, symbol, expected):
        assert string_utils.contains(string, symbol) == expected


class TestDeleteSymbol:

    @pytest.mark.positive
    @pytest.mark.parametrize(
        "string, symbol, expected",
        [
            ("SkyPro", "k", "SyPro"),
            ("SkyPro", "Pro", "Sky"),
            ("hello world", " ", "helloworld"),
            ("banana", "a", "bnn"),
            ("04 апреля 2023", "2023", "04 апреля "),
            ("12345", "3", "1245"),
            ("тест", "т", "ес"),
        ],
    )
    def test_delete_symbol_positive(self, string, symbol, expected):
        assert string_utils.delete_symbol(string, symbol) == expected

    @pytest.mark.negative
    @pytest.mark.parametrize(
        "string, symbol, expected",
        [
            ("", "a", ""),
            ("   ", "a", "   "),
            ("test", "", "test"),
            ("", "", ""),
            ("hello", "x", "hello"),
            ("123", "4", "123"),
        ],
    )
    def test_delete_symbol_negative(self, string, symbol, expected):
        assert string_utils.delete_symbol(string, symbol) == expected


class TestEdgeCases:

    def test_capitalize_single_character(self):
        assert string_utils.capitalize("a") == "A"
        assert string_utils.capitalize("") == ""

    def test_trim_no_spaces(self):
        assert string_utils.trim("skypro") == "skypro"
        assert string_utils.trim("") == ""

    def test_contains_special_symbols(self):
        assert string_utils.contains("hello!@#", "!") == True
        assert string_utils.contains("hello!@#", "@") == True

    def test_delete_symbol_all_occurrences(self):
        assert string_utils.delete_symbol("aaaa", "a") == ""
        assert string_utils.delete_symbol("a b a b a", "a") == " b  b "
