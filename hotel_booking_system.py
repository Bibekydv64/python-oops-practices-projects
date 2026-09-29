class HotemBookingSystem:

    def __init__(self):
        self.database = {}
        self.room_number_database = []
        self.menu()
    



    def menu(self):
        while True:
            user_input_chose = input('''
            ===== HOTEL MANAGEMENT SYSTEM =====
            1. Add Room
            2. View Rooms
            3. Book Room
            4. Search Booking
            5. Check-in
            6. Check-out
            7. Cancel Booking
            8. Exit
            ===================================
            chose a number:''')

            if user_input_chose == '1':
                self.add_room()
            elif user_input_chose == '2':
                self.view_room()
            
            elif user_input_chose == '3':
                pass

            elif user_input_chose == '4':
                pass

            elif user_input_chose == '5':
                pass

            elif user_input_chose == '6':
                pass

            elif user_input_chose == '7':
                pass

            elif user_input_chose == '8':
                print('Exit sucesfully')
                break



    def add_room(self):
        add_room_number = int(input('Enter add room'))
        for room in range(add_room_number):
            room_number = int(input('Enter a room number'))
            if room_number not in self.room_number_database:
                self.room_number_database.append(room_number)
                print('store datasucesfully')
            else:
                print(add_room_number,'Available in databased')
    

    def view_room(self):
        print(f'Total Room available:{self.room_number_database}')


    def book_room(self):
        pass

    def search_room(self):
        pass

    def cheakin_room(self):
        pass

    def cheakout_room(self):
        pass


    def cancel_room(self):
        pass


HotemBookingSystem_obj = HotemBookingSystem()
print(HotemBookingSystem_obj)