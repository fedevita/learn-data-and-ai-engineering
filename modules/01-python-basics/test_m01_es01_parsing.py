import pytest
from es01_parsing import parse_amount, parse_date


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("12,50", 12.5),
        ("-12,50", -12.5),
        ("1.234,56", 1234.56),
        ("0,00", 0.0),
        ("  7,10  ", 7.1),
        ("100", 100.0),
    ],
)
def test_parse_amount_converts_italian_format(text, expected):
    assert parse_amount(text) == pytest.approx(expected)


@pytest.mark.parametrize("text", ["", "abc", "12,5,0"])
def test_parse_amount_rejects_invalid_input(text):
    with pytest.raises(ValueError):
        parse_amount(text)


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("31/12/2024", "2024-12-31"),
        ("01/02/2025", "2025-02-01"),
        ("5/3/2025", "2025-03-05"),
    ],
)
def test_parse_date_converts_to_iso(text, expected):
    assert parse_date(text) == expected


@pytest.mark.parametrize("text", ["2024-12-31", "31-12-2024", "31/02/2024", "ciao"])
def test_parse_date_rejects_invalid_input(text):
    with pytest.raises(ValueError):
        parse_date(text)
