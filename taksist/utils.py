from django.contrib.auth.models import User

def user_photo_upload_path(instance, filename):
    user_id=instance.User.id
    return 'user_photos/user_{0}/{1}'.format(user_id, filename)

def car_photo_upload_path(instance, filename):
    user_id=instance.User.id
    return 'car_photos/user_{0}/{1}'.format(user_id, filename)