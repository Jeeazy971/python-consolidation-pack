existing_users = ["alice", "bob", "chloe"]
imported_users = ["bob", "chloe", "dylan", "emma"]


def get_new_users(existing_users, imported_users):
    return sorted(set(imported_users) - set(existing_users))


print(get_new_users(existing_users, imported_users))  # ["dylan", "emma"]
print(get_new_users(existing_users, existing_users))  # []
