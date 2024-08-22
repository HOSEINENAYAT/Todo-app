import functions
import PySimpleGUI as sg
import time

clock=sg.Text(time.strftime("%b %d %y %H %M:%S"),key="clock")
label=sg.Text("type in a to_do")
input_box=sg.InputText(tooltip="Enter a to_do",key="todo")
add_button=sg.Button("Add")
list_box=sg.Listbox(values=functions.get_todos(),key="todos",
                    enable_events=True,size=[45,10])
edit_button=sg.Button("Edit")
complete_button=sg.Button("Complete")
exit_button=sg.Button("Exit")
window=sg.Window("my To_do App",
                 layout=[
                     [clock],
                     [label],
                     [input_box,add_button],
                     [list_box,edit_button,complete_button],
                     [exit_button]
                 ],font=("Helvetica",20))


while True:
    event,values=window.read(timeout=20)
    window['clock'].update(value= time.strftime("%b %d %y %H %M:%S"))
    print(event,values)

    match event:
        case "Add":
            todos=functions.get_todos()
            new_todo=values['todo']+'\n'
            todos.append(new_todo)
            functions.set_todos(todos)
            window["todos"].update(values=todos)
        case "Edit":
            todos=functions.get_todos()
            todo_to_edit=values['todos'][0]
            index=todos.index(todo_to_edit)
            todos[index]=values['todo']
            functions.set_todos(todos)
            window["todos"].update(values=todos)
        case"todos":
            window['todo'].update(value=values['todos'][0])
        case"Complete":
            todos=functions.get_todos()
            todo_to_complete=values['todos'][0]
            todos.remove(todo_to_complete)
            functions.set_todos(todos)
            window["todos"].update(values=todos)
        case sg.WIN_CLOSED:
            exit()
window.close()