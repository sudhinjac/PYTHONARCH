import logging

# =========================
# LOGGING CONFIG
# =========================

logger = logging.getLogger(__name__)


class TooManyStudents(Exception):
    pass


class Classroom:

    MAX_STUDENTS = 10

    def __init__(self, teacher, students, course_title):
        self.teacher = teacher
        self.students = students
        self.course_title = course_title

    def add_student(self, student):
        if len(self.students) >= self.MAX_STUDENTS:
            logger.error(
                f"Cannot add {student.name}. Classroom '{self.course_title}' is full."
            )
            raise TooManyStudents("Class is full")

        self.students.append(student)
        logger.info(
            f"Student '{student.name}' added to '{self.course_title}'. Total students: {len(self.students)}"
        )
        return True

    def remove_student(self, name):
        for student in self.students:
            if student.name == name:
                self.students.remove(student)
                logger.info(
                    f"Student '{name}' removed from '{self.course_title}'. Remaining students: {len(self.students)}"
                )
                return True

        logger.warning(
            f"Attempted to remove '{name}' but student not found in '{self.course_title}'."
        )
        return False

    def change_teacher(self, new_teacher):
        logger.info(
            f"Teacher changed from '{self.teacher}' to '{new_teacher}' for '{self.course_title}'."
        )
        self.teacher = new_teacher
        return True


class Person:
    def __init__(self, name):
        self.name = name


class Student(Person):
    pass