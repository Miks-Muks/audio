import os


def get_path_upload_cover_album(instance, file):
    return f'album/user_{instance.user.id}/{file}'


def get_path_upload_cover_playlist(instance, file):
    return f'playlist/user_{instance.user.id}/{file}'


def get_path_upload_track(instance, file):
    return f'track/user_{instance.user.id}/{file}'


def get_path_upload_cover_track(instance, file):
    return f'trac/cover/user_{instance.user.id}/{file}'


def delete_old_file(path_file):
    if os.path.exists(path_file):
        os.remove(path_file)


def test(value: str, name) -> bool:
    if value is None:
        return False
    return True
