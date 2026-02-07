from courses.models import Course

class CourseRepository:
    def create_course(self, title, description, instructor):
        return Course.objects.create(title=title, description=description, instructor=instructor)

    def get_course_by_id(self, course_id):
        try:
            return Course.objects.get(id=course_id)
        except Course.DoesNotExist:
            return None

    def update_course(self, course_id, **kwargs):
        course = self.get_course_by_id(course_id)
        if course:
            for key, value in kwargs.items():
                setattr(course, key, value)
            course.save()
            return course
        return None

    def delete_course(self, course_id):
        course = self.get_course_by_id(course_id)
        if course:
            course.delete()
            return True
        return False
    
    def list_courses(self):
        return Course.objects.all()
    
    def enroll_student(self, course_id, student):
        course = self.get_course_by_id(course_id)
        if course:
            course.students.add(student)
            return True
        return False
    
    def unenroll_student(self, course_id, student):
        course = self.get_course_by_id(course_id)
        if course:
            course.students.remove(student)
            return True
        return False
    
    def get_students_in_course(self, course_id):
        course = self.get_course_by_id(course_id)
        if course:
            return course.students.all()
        return None
    
    def is_course_for_instructor(self, course_id, instructor):
        course = self.get_course_by_id(course_id)
        if course:
            return course.instructor == instructor
        return False