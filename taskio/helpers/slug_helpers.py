def get_task_slug(instance):
    return f"task-{str(instance.uid).split('-')[0]}"
