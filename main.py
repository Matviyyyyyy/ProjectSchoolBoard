import django_setup
from project.models import Subject, Student, Class, Teacher

subject1 = Subject(
    title = "Algebra"
)
subject1.save()

subject3 = Subject(
    title = "Geometry"
)
subject3.save()


teacher1 = Teacher(
    first_name = "Maryana",
    last_name = "Myroslavivna",
    email = "maryanamyr@gmail.com",)
teacher1.save()

subject1.teachers.add(teacher1)
subject3.teachers.add(teacher1)

subject2 = Subject(
    title = "Ukraininan"
)
subject2.save()

teacher2 = Teacher(
    first_name = "Maria",
    last_name = "Bohdanivna",
    email = "mariabohd@gmail.com")

teacher2.save()

subject2.teachers.add(teacher2)



class1 = Class(
   name = "9-В"
)
class1.save()

student1 = Student(
    first_name = "Matviy",
    last_name = "Gura",
    email = "matviy@gmail.com",
    class_id = class1
).save()

student2 = Student(
    first_name = "Max",
    last_name = "Lychun",
    email = "maxlychun@gmail.com",
    class_id = class1
    ).save()

class2 = Class(
    name = "9-A"
)
class2.save()

student4 = Student(
    first_name = "Oleh",
    last_name = "Kyrov",
    email = "olehkyrov@gmail.com",
class_id = class2
).save()

student5 = Student(
    first_name = "Anna",
    last_name = "Ivanyk",
    email = "annaivanyk@gmail.com",
    class_id = class2
).save()

student6 = Student(
    first_name = "Vika",
    last_name = "Chnur",
    email = "vikachnur@gmail.com",
    class_id = class2
).save()