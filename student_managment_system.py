class StudentManagmentSystem:

    def __init__(self):
        print('Welcome to student management system')
        self.database1 = {}
        self.menu()



    def menu(self):
        user_menu_input = input('''
        ===========MENU==========
        1. press 1 to Add Student
        2. press 2 to view student 
        3. press 3 to search student
        4. press 4 to update student
        5. press 5 to delete student
        6. press intteger to Exit this program
        =======================================
        chose a number:
        ''')


        if user_menu_input == '1':
            self.Add_student()

        elif user_menu_input == '2':
            self.view_student()

        elif user_menu_input == '3':
            self.search_student()

        elif user_menu_input == '4':
            self.upadate_student()

        elif user_menu_input == '5':
            self.delete_student

        else:
            print('Program exit sucessfully')


    def Add_student(self):
        user_student_number = int(input('Enter a number how much add:'))
        for add in user_student_number:
            if add not in self.database1.keys():
                self.database1['Name'] = add
                print('current store student:',self.database1)
            else:
                print('this student already Exits') 


            # user_student_number = int(input('add student count:'))
            # for num in range(user_student_number+1):
            #     self.user_student_Id = int(input('Enter StudentID:'))
            #     self.user_student_name = input('Enter student Name:')
            #     self.user_student_age = int(input('Enter student Age:'))
            #     self.user_student_Total_marks = int(input('Enter student total marks:'))

            #     self.database[num] = {
            #         'studentID': self.user_student_id,
            #         'student Name':self.user_student_name,
            #         'student Age' : self.user_student_age,
            #         'student total name': self.user_student_Total_marks
            #         }


    def view_student(self):
        print(f'Your record name:{self.database1}')


    def  search_student(self):
        user_search_student = input('Enter searchb student name:')
        if user_search_student in self.database1.keys():
            print(user_search_student,'is already present')
        else:
            print('student not present')

    def upadate_student(self):
        pass
    def delete_student(self):
        pass



StudentManagmentSystem_obj = StudentManagmentSystem()

print(StudentManagmentSystem_obj)







