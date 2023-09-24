class Student:
    def __init__(self):
        self.students = []  # Initialize an empty list to store student names

    def add_student(self, student_name):
        self.students.append(student_name)  # Add a student to the list

    def mark_attendance(self, student_name):
        for i, student in enumerate(self.students):
            if student == student_name:
                self.students[i] = (student, True)  # Mark attendance as True for the student

    def display_attendance(self):
        for student, attendance_status in self.students:
            status = "Present" if attendance_status else "Absent"
            print(f"{student}: {status}")

def main():
    stud = Student()

    while True:
        print("\nOptions:")
        print("1. Add Student")
        print("2. Mark Attendance")
        print("3. Display Attendance")
        print("4. Quit")

        option = input("Enter your choice: ")

        if option == "1":
            naming = input("Enter Student Name: ")
            stud.add_student(naming)
        elif option == "2":
            marking = input("Enter Student Name: ")
            stud.mark_attendance(marking)
        elif option == "3":
            stud.display_attendance()
        elif option == "4":
            break

if __name__ == "__main__":
    main()
