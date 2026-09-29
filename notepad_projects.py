# 🎯 Goal
# Build a terminal-based Notepad where the user can create, view, edit, search, and delete notes.
# Features
# ==============================
#         CLI NOTEPAD
# ==============================
# 1. Create Note
# 2. View All Notes
# 3. View Single Note
# 4. Edit Note
# 5. Search Note
# 6. Delete Note
# 7. Delete All Notes
# 8. Exit

# Choose an option:
# 🧩 Required Features


# 1. Create Note
# Ask for note title
# Ask for note content
# Automatically generate a unique note ID
# Save the note permanently
# Example:
# Title: Python OOP
# Content: Today I learned encapsulation.
# Note created successfully!

# 2. View All Notes
# ID: 1 | Title: Python OOP
# ID: 2 | Title: Shopping List
# ID: 3 | Title: College Tasks

# 3. View Single Note
# Ask for note ID
# Display:
# ID
# Title
# Content
# Created date/time

# 4. Edit Note
# Ask for note ID
# Allow changing:
# Title
# Content

# 5. Search Note
# Search by title or content.
# Example:
# Search: Python
# Found:
# ID: 1
# Title: Python OOP
# Content: Today I learned encapsulation.

# 6. Delete Note
# Ask for note ID
# Delete only that note.

# 7. Delete All Notes
# Ask for confirmation:
# Are you sure? (yes/no):

# 8. Exit
# Thank you for using CLI Notepad!
# 🏗️ Suggested OOP Architecture

# Don't write everything in one class.
# Note
#  ├── note_id
#  ├── title
#  ├── content
#  └── created_at
# Notepad
#  ├── create_note()
#  ├── view_notes()
#  ├── view_note()
#  ├── edit_note()
#  ├── search_note()
#  ├── delete_note()
#  └── delete_all_notes()
# FileManager
#  ├── load_notes()
#  └── save_notes()
# 💾 Storage



# Use:
# notes.json

# Example structure:
# [
#     {
#         "id": 1,
#         "title": "Python OOP",
#         "content": "Today I learned encapsulation.",
#         "created_at": "2026-09-22"
#     }
# ]
import json

class NotePad:
    def __init__(self):
        self.__notepad_database = []
        self.Menu()

    def __str__(self):
        print("Welcome To Note Pad Cli Projects:")


    def Menu(self):
        User_input = input('''
         ==============================
                CLI NOTEPAD
         ==============================
         1. Create Note
         2. View All Notes
         3. View Single Note
         4. Edit Note
         5. Search Note
         6. Delete Note
         7. Delete All Notes
         8. Exit
         ''')

        if User_input == '1':
            self.Create_note()

        elif User_input == '2':
            self.View_All_Notes()
        
        elif User_input == '3':
            self.View_Single_Note()

        elif User_input == '4':
            self.Edit_Note()

        elif User_input == '5':
            self.Search_Note()

        elif User_input == '6':
            self.Delete_Note()

        elif User_input == '7':
            self.Delete_All_Notes()

        elif User_input == '8':
            print('Exit sucessfully Sir')

        else:
            print('Envalid keyword Try again later')
# Title: Python OOP
# Content: Today I learned encapsulation.
# Note created successfully!


    def Create_note(self):
        try:
            note_title = input('Enter a Note Title:')
            Note_content = input('Enter a Content:')
            Note_date_content = input('Enter a content Date:')

            Note_content ={'note_title': note_title,
                        'note_content': Note_content,
                        'note_date': Note_date_content
                        }
            self.__notepad_database.append(Note_content)
        
            with open('database.json','a') as file:
                json.dump(Note_content,file,indent=4)
        except:
            print('This is runtime Error Try again')
        finally:
            print('Note created sucessfully:')


    def View_All_Notes(self):
        try:
            with open('database.json','r') as file:
                data = json.load(file)
                print(data)

        except:
            print('This is runtime error try again:')

        finally:
            print('database load sucessfully')

    def View_Single_Note(self):
        try:
            with open('database.json','r') as file:
                data = json.load(file)
                user_input = input('Enter a Search Note:')
                if data['note_title'] == user_input.lower():
                    print(f"Note Title:{data['note_title']}")
                    print(f"Note Content:{data['note_content']}")
                    print(f"Note date:{data['note_date']}")
                else:
                    print('Not found')
        except:
            print('Runtime Error problem')

    def Edit_Note(self):
        User_input = input('enter a Note Title:')

        with open('database.json','r') as file:
            data = json.load(file)

            if data['note_title'] == User_input.lower():
                print("=================================")
                print(f"1. Note Title:{data['note_title']}")
                print(f"2. Note Content:{data['note_content']}")
                print(f"3. Note date:{data['note_date']}")
                print("=================================")
            else:
                print('Note title not Found:')

            User_input1 = input('chose What you Want to Change:')

            if User_input1 == data['note_title']:
                user_title_input_new = input('Enter Title Name:')
                with open('database.json','w') as file1:
                    data['note_title'] =user_title_input_new
                    json.dump(data,file1)
                    print('Note Title Edited Sucessfully:')


            elif User_input1 == data['note_content']:
                user_title_input_new = input('Enter Title Name:')

                with open('database.json','w') as file2:
                    user_content_input_new = input('Enter Note content:')
                    data['note_content'] = user_content_input_new
                    json.dump(data,file2)
                    print('Note Title Edited Sucessfully:')

            elif User_input1 == data['note_date']:
                with open('database.json','w') as file3:
                    user_content_input_new = input('Enter Note Date:')
                    data['note_date'] = user_content_input_new
                    json.dump(data,file3)
                    print('Note Title Edited Sucessfully:')
            else:
                print('Invalid KeyWord Write propely Cli Name')

    def Search_Note(self):
        pass

    def Delete_Note(self):
        pass

    def Delete_All_Notes(self):
        pass


NotePad_obj = NotePad()
print(NotePad)






