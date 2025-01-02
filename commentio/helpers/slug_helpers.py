
def get_task_comment_slug(instance):
    return f"task-comment-{str(instance.uid).split('-')[0]}"