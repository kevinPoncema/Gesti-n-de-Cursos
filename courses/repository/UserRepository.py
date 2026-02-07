from courses.models import User

class UserRepository:
    def create_user(username, email, password,role='student'):
        return User.objects.create_user(username=username, email=email, password=password,role=role)
         

    def get_user_by_id(user_id):
        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist:
            return None

    def get_user_by_username(username):
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            return None
        
    def update_user(user_id, **kwargs):
        user = UserRepository.get_user_by_id(user_id)
        if user:
            for key, value in kwargs.items():
                setattr(user, key, value)
            user.save()
            return user
        return None

    def delete_user(user_id):
        user = UserRepository.get_user_by_id(user_id)
        if user:
            user.delete()
            return True
        return False