# Validating Card Number

import re


def get_valid_card_number(s=str):
    try:
        assert re.search(r"^(4|5|6)", s)
        assert len("".join(s.split("-"))) == 16
        assert len(re.findall(r"-", s)) == 3 or len(re.findall(r"-", s)) == 0
        assert len(re.findall(r"\d{4}", s)) == 4
        assert not re.search(r"[^0-9-]", s)
        assert not re.search(r"(-)\1", s)
        assert not re.search(r"(\d)\1{3}", "".join(s.split("-")))
    except AssertionError as ae:
        return "Invalid"
    else:
        return "Valid"


if __name__ == "__main__":

    for _ in range(int(input())):
        s = input()
        print(get_valid_card_number(s))

