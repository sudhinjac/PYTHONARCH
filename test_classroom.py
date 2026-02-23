import pytest
import school as s



# =========================
# FIXTURES
# =========================

@pytest.fixture
def teacher():
    return "Mr. Smith"


@pytest.fixture
def students():
    return [s.Student("Alice"), s.Student("Bob")]


@pytest.fixture
def classroom(teacher, students):
    return s.Classroom(teacher, students, "Math")


# =========================
# TESTS
# =========================

def test_add_student(classroom):
    new_student = s.Student("Charlie")
    classroom.add_student(new_student)
    assert new_student in classroom.students


def test_add_student_raises():
    students = [s.Student(f"S{i}") for i in range(10)]
    classroom = s.Classroom("Teacher", students, "Science")

    with pytest.raises(s.TooManyStudents):
        classroom.add_student(s.Student("Extra"))


@pytest.mark.parametrize("name", ["Alice", "Bob"])
def test_remove_student(classroom, name):
    classroom.remove_student(name)
    assert all(student.name != name for student in classroom.students)


def test_change_teacher(classroom):
    classroom.change_teacher("Mrs. Johnson")
    assert classroom.teacher == "Mrs. Johnson"


@pytest.mark.slow
def test_bulk_add():
    classroom = s.Classroom("Teacher", [], "History")

    for i in range(10):
        classroom.add_student(s.Student(f"S{i}"))

    assert len(classroom.students) == 10