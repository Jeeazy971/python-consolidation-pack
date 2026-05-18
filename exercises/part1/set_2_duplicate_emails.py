emails = ["a@example.com", "b@example.com",
          "a@example.com", "c@example.com", "b@example.com"]


def find_duplicate_emails(emails):
    seen_emails = set()
    duplicate_emails = set()
    
    for email in emails:
        if email in seen_emails:
            duplicate_emails.add(email)
        else:
            seen_emails.add(email)
    return sorted(duplicate_emails)


print(find_duplicate_emails(emails))   # ["a@example.com", "b@example.com"]
print(find_duplicate_emails([]))       # []
