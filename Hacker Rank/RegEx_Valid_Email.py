# validating email addresses with a filter
import re


def fun(s):
    valid_email = re.finditer(r"[A-Za-z0-9_-]+@[A-Za-z0-9]+\.(.|..|...)$", s)

    for match in valid_email:
        if match.group() == s:
            return True
        else:
            return False


def filter_mail(emails):
    return list(filter(fun, emails))


if __name__ == "__main__":
    n = int(input())

    emails = []

    for _ in range(n):
        emails.append(input())

    filtered_emails = filter_mail(emails)
    filtered_emails.sort()
    print(filtered_emails)
