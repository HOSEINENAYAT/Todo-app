# import functions
from functions import get_todos,set_todos


user_prompt="enter a todo: "
todos = []

while True:
    user_action=input("Enter add,show,edit,complete or exit: ")
    if user_action.startswith("add"):
            todos=get_todos()
            todo=user_action[4:]+"\n"
            todos.append(todo)
            set_todos(todos)
    if user_action.startswith("show"):
        todos=get_todos()
        for index,todo in enumerate(todos):
            print(index+1,"-",todo)
    if user_action.startswith("edit"):
            break
    if user_action.startswith("complete"):
            todos=get_todos()
            todo=user_action[9:]+"\n"
            number=input("Enter a number of todo to complete:")
            todos.pop(int(number)-1)
            set_todos(todos)
    if user_action.startswith("edit"):
        try:
            todos=get_todos()
            number=user_action[5:]+"\n"
            new_todo=input("edit this todo here: ")
            todos[int(number)-1]=new_todo
            set_todos(todos)
        except IndexError:
            print("your Index is out of range")

print("Done!")
# filenames=["1.word.txt","2.photoshop.txt","3.excel.txt"]add
#
# for filename in filenames:
#     print(filename.replace(".","-",))