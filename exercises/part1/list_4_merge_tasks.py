morning_tasks = ["emails", "standup"]
afternoon_tasks = ["coding", "review"]


def merge_tasks(list_a, list_b):
    return list_a + list_b


# ["emails", "standup", "coding", "review"]
print(merge_tasks(morning_tasks, afternoon_tasks))
print(merge_tasks([], ["a", "b"]))                  # ["a", "b"]
