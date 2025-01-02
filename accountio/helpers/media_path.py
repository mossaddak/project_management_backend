def get_user_media_path_prefix(instance, filename):
    return f"media/user/{instance.username}/profile-picture/{filename}"
