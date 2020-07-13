# ginortS
import re


def special_sort(s=""):
    result = ""
    patterns = [r"[a-z]", r"[A-Z]", r"[13579]", r"[02468]"]
    for item in patterns:
        matches = re.findall(item, s)
        text = ""
        # matching all patterns
        for match in matches:
            text += match

        # sorted all string
        for sort in list(sorted(text)):
            result += sort
    return result


if __name__ == "__main__":
    text_to_sort = input()
    print(special_sort(text_to_sort))
