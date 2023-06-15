import functions
import PySimpleGUI as sg
label=sg.Text("Enter a Todo in list")
input_text=sg.InputText(tooltip="please enter a todo",key="todo")
add_btn=sg.Button("ADD")
window=sg.Window("QAZI's Todo APP",
                 layout=[[label],[input_text,add_btn]],
                 font=('Helvetica',12))
while True:
    event,values=window.read()
    print(event)
    print(values)
    match event:
        case "ADD":
            todolist=functions.get_todolist()
            new_todo=values['todo'] + '\n'
            todolist.append(new_todo)
            functions.write_todolist(todolist)
        case sg.WINDOW_CLOSED:
            break
window.close()

