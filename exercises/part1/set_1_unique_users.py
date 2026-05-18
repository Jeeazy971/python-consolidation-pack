users = ["alice", "bob", "alice", "chloe", "bob", "dylan"]


def get_unique_users(users):
    unique_users = set()
    
    for user in users:
        unique_users.add(user)
        
    return sorted(unique_users)


print(get_unique_users(users))  # ["alice", "bob", "chloe", "dylan"]
print(get_unique_users([]))     # []
