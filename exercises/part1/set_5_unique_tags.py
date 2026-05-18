articles = [
    {"title": "Python basics", "tags": ["python", "beginner"]},
    {"title": "FastAPI intro", "tags": ["python", "api", "backend"]},
    {"title": "Clean code", "tags": ["backend", "quality"]},
]


def get_unique_tags(articles):
    unique_tags = set()

    for article in articles:
        for tag in article["tags"]:
            unique_tags.add(tag)

    return sorted(unique_tags)

print(get_unique_tags(articles))  # ["api", "backend", "beginner", "python", "quality"]
print(get_unique_tags([]))        # []
