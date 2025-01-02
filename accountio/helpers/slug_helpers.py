def get_user_slug(instance):
    return f"{instance.username}-{str(instance.uid).split('-')[0]}"