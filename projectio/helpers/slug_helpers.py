def get_project_slug(instance):
    return f"project-{str(instance.uid).split('-')[0]}"


def get_project_member_slug(instance):
    return f"project-member-{str(instance.uid).split('-')[0]}"
