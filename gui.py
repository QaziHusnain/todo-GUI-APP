import functions
import PySimpleGUI as sg
label=sg.Text("Enter a Todo in list")
input_text=sg.InputText(tooltip="please enter a todo",key="todo")
add_btn=sg.Button("ADD")
list_box=sg.Listbox(values=functions.get_todolist(),
                    key='todos',enable_events=True,size=[45,10])
edit_btn=sg.Button("EDIT")
window=sg.Window("QAZI's Todo APP",
                 layout=[[label],[input_text,add_btn],[list_box,edit_btn]],
                 font=('Helvetica',12))
while True:
    event,values=window.read()
    print(event)
    print(values)


    match event:
        case "ADD":
            todolist = functions.get_todolist()
            new_todo = values['todo']+ "\n"
            todolist.append(new_todo)
            functions.write_todolist(todolist)
            window['todos'].update(values=todolist)
        case "EDIT":

            todo_to_edit=values['todos'][0]
            new_todo=values['todo']


            todolist=functions.get_todolist()
            index_to_edit=todolist.index(todo_to_edit)

            todolist[index_to_edit] = new_todo
            functions.write_todolist(todolist)
            window['todos'].update(values=todolist)
        case "todos":

            window['todo'].update(value=values['todos'][0])


        case sg.WINDOW_CLOSED:
            break
window.close()

