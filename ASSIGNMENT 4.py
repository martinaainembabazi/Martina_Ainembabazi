#UNIVERSITY SYSTEM
class Person:
    def __init__(self,reg_number):
        self.reg_number=reg_number
        
    

class Student(Person):
    def __init__(self, reg_number,student_name,student_id,course):
        super().__init__(reg_number)
        self.student_name=student_name
        self.student_id=student_id
        self.course=course

class Lecturer(Person):
    def __init__(self, reg_number,lecturername,lecturer_id,course):
        super().__init__(reg_number)
        self.lecturername=lecturername
        self.lecturer_id=lecturer_id
        self.course=course





class Staff(Person):
    def __init__(self, reg_number,staffname,staff_id):
        super().__init__(reg_number)
        self.staffname=staffname
        self.staff_id=staff_id

class UniversitySystem:
    def __init__ (self):
        self.students=[]
        self.lecturers=[]
        self.staff_members=[]

    def add_student(self,reg_number,student_name,student_id,course):
        student=Student(reg_number, student_name, student_id, course)
        self.students.append(student)

    def add_lecturer(self, reg_number, lecturername, lecturer_id, course):
        lecturer = Lecturer(reg_number, lecturername, lecturer_id, course)
        self.lecturers.append(lecturer)

    def add_staff(self, reg_number, staffname, staff_id):
        staff = Staff(reg_number, staffname, staff_id)
        self.staff_members.append(staff)

    def list_all(self):
        print("=== Students ===")
        for s in self.students:
            print(f"{s.student_name} ({s.student_id}) - {s.course}")

        print("\n=== Lecturers ===")
        for l in self.lecturers:
            print(f"{l.lecturername} ({l.lecturer_id}) - {l.course}")

        print("\n=== Staff ===")
        for st in self.staff_members:
            print(f"{st.staffname} ({st.staff_id})")         
    
s=UniversitySystem()
s.add_lecturer("DE7879","Peter","S101","Artificial Intelligence")
s.add_staff("ST6898","Carol","SA8138")
s.add_student("S3209","Martha","HT890","Computer Science")
s.list_all()
                        