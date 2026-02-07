from courses.repository import UserRepository
class AuthService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def register_student(self,data):
        return self.user_repository.create_user(data['username'], data['email'], data['password'], role='student')
    
    def register_user(self,data,request):
        if not request.user.is_authenticated or request.user.role != 'admin':
            raise PermissionError("Only admin users can register new users.")
        
        return self.user_repository.create_user(data['username'], data['email'], data['password'], data['role'])
    

