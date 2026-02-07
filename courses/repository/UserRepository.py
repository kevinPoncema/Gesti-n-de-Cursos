from courses.models import User

class UserRepository:
    def create_user(self, username, email, password, role='student'):
        return User.objects.create_user(username=username, email=email, password=password, role=role)

    def get_user_by_id(self, user_id):
        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist:
            return None

    def get_user_by_username(self, username):
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            return None
        
    def update_user(self, user_id, **kwargs):
        user = self.get_user_by_id(user_id)
        if user:
            for key, value in kwargs.items():
                setattr(user, key, value)
            user.save()
            return user
        return None

    def delete_user(self, user_id):
        user = self.get_user_by_id(user_id)
        if user:
            user.delete()
            return True
        return False