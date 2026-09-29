# ================================
#        SECURE BANK SYSTEM
# ================================

# 1. Register User
# 2. Login
# 3. Create Bank Account
# 4. Deposit
# 5. Withdraw
# 6. Check Balance
# 7. ATM
# 8. Change Password
# 9. Change PIN
# 10. Account Information
# 11. Logout
# 12. Exit

# Enter your choice:


class Bank:
    def __init__(self):
        self.counter_registor_database = 0
        self.__registor_database = {}
        self.__login_Username = 'bibek'
        self.__login_password = 'bibek@12'
        self.__Atm_pin = '1234'
        self.__balance = 2000
        self.menu()


    def menu(self):
        user_menu_input = input('''
        ================================
            SECURE BANK SYSTEM
        ================================
        1. Register User
        2. Login 
        3. Create Bank Account
        4. Deposit
        5. Withdraw
        6. Check Balance
        7. ATM
        8. Change Password
        9. Change PIN
        10. Account Information
        11. Logout
        12. Exit
        Enter your choice:
        ''')


        if user_menu_input == '1':
            self.Register_User_method()

        elif user_menu_input == '2':
            self.Login_method()

        elif user_menu_input == '3':
            self.Create_bank_account_method()
            
        elif user_menu_input == '4':
            self.Deposite_method()

        elif user_menu_input == '5':
            self.Withdrowl_method()

        elif user_menu_input == '6':
            self.Atm_method()

        elif user_menu_input == '7':
            self.Atm_method_method()

        elif user_menu_input == '8':
            self.Change_password_method()

        elif user_menu_input == '9':
            self.Change_Pin_method()

        elif user_menu_input == '10':
            self.Account_information_method()

        elif user_menu_input == '11':
            self.Logout_method()
        elif user_menu_input == '12':
            self.Exit_method()
        else:
                print('Wrong keyword typing')


    def Register_User_method(self):
        print('''Welcome in Bibek bank:
please register you account sir
        '''.upper())
        user_name_register = input('Enter a name:')
        user_password_register = input('Enter a password for ragister:')
        counter_result = self.__counter_registor_database +1
        self.registor_database['Register Name:',counter_result]={'Name':user_name_register,'User_password':user_password_register}
        print('Congracts Sir Account Register sucessfully:')

    def Login_method(self):
        user_name_input = input('Enter a username:')
        user_password_input = input('Enter a Password:')

        if user_name_input == self.__login_Username and self.__login_password == user_password_input:
            print('Login Sucessfully:')
        else:
            print('Wrong password and usename:')



    def Create_bank_account_method(self):
        self.user_name =input('Enter a name:')
        self.user_last_name = input('ENter a last name:')
        self.user_age = input('Enter a age:')
        self.user_gender = input('Enter a Sex:')
        self.user_citizinship_number = input('Enter a Citizinship Number:')
        self.account_number = input('chose a account number:')
        print('account Created sucessfully sir:')

    def Deposite_method(self):
        self.user_input_for_deposite = int(input("Enter a Deposite number:"))
        self.__balance += self.user_input_for_deposite
        print(f"Deposite sucessfully sir\nYour total Balance:{self.__balance}")


    def Withdrowl_method(self):
        user_withdrowl_balance_input = input('Enter a withdrowl balance:')
        if self.__balance < user_withdrowl_balance_input:
            print('withdrowl sucessfully:')
        else:
            print('Insufficet balance:')

    def cheak_balance(self):
        return (F"Your Balance:{self.__balance}")


    def Atm_method_method(self):
        print('nothing Pass')

    def Change_password_method(self):
        user_old_password = input('Enter a old password:')
        if user_old_password == self.__login_password:
            new_password = input('Enter anew password:')
            self.__login_password = new_password
            print(self.__login_password)

        
    def Change_Pin_method(self):
        user_old_pin = input('Enter a old pin:')
        if user_old_pin == self.__Atm_pin:
            new_pin = input('Enter anew password:')
            self.__Atm_pin= new_pin
            print(self.__Atm_pin)
        else:
            print('Pin wrong Try again:')

    def Account_information_method(self):
        self.Create_bank_account_method()

    def Logout_method(self):
        print('Logout sucesfully:')

    def Exit_method(self):
        print('Exit sucessfully:')
    

obj = Bank()
print(obj)     

  













































































