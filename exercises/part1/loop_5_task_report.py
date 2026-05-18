tasks = [
    {"title": "Fix bug", "done": True},
    {"title": "Write docs", "done": False},
    {"title": "Add tests", "done": True},
]


def build_task_report(tasks):
    tasks_report = []
    
    for task in tasks:
        report_task = task['title']
        if task['done']:
            tasks_report.append("✅ " + report_task)
        else:
            tasks_report.append("❌ " + report_task)
    return tasks_report


print(build_task_report(tasks))  # ["✅ Fix bug", "❌ Write docs", "✅ Add tests"]
print(build_task_report([]))     # []
