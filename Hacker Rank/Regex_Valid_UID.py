# Validating UID

import re


def get_valid_uid(s=str):
    try:
        assert re.search(r"[A-Z]{2}", s)
        assert re.search(r"\d\d\d", s)
        assert not re.search(r"[^a-zA-Z0-9]", s)
        assert not re.search(r"(.)\1", s)
        assert len(s) == 10
    except AssertionError as ae:
        return "Invalid"
    else:
        return "Valid"


if __name__ == "__main__":

    for _ in range(int(input())):
        s = "".join(sorted(input()))
        print(get_valid_uid(s))
