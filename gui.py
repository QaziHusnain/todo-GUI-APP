import functions
import PySimpleGUI as sg
label=sg.Text("Enter a Todo in list")
input_text=sg.InputText(tooltip="please enter a todo",key="todo")
add_btn=sg.Button("ADD")
list_box=sg.Listbox(values=functions.get_todolist(),
                    key='todos',enable_events=True,size=[45,10])
edit_btn=sg.Button("EDIT")
complete_btn=sg.Button("COMPLETE")
exit_btn=sg.Button("EXIT")
window=sg.Window("QAZI's Todo APP",
                 layout=[[label],[input_text,add_btn],[list_box,edit_btn,complete_btn],[exit_btn]],
                 font=('Helvetica',12))
while True:
    event,values=window.read()
    #print(event)



    match event:
        case "ADD":

            todolist = functions.get_todolist()
            new_todo = values['todo']+ "\n"
            blank_string=new_todo.strip()
            blank_check=len(blank_string)

            if blank_check>0:

                todolist.append(new_todo)
                functions.write_todolist(todolist)
                window['todos'].update(values=todolist)
            else:
                sg.popup("please first enter then add")
        case "EDIT":
            try:

                todo_to_edit=values['todos'][0]
                new_todo=values['todo']+'\n'
                blank_string=new_todo.strip()
                blank_check=len(blank_string)
                print=len(values['todo'])


                if blank_check>0 and new_todo.strip()!=todo_to_edit.strip():



                    todolist=functions.get_todolist()
                    index_to_edit=todolist.index(todo_to_edit)

                    todolist[index_to_edit] = new_todo
                    functions.write_todolist(todolist)
                    window['todos'].update(values=todolist)
                else:
                    sg.popup("Please first enter then press EDIT",font=['Helvetica',14])
            except IndexError:
                sg.popup("Please select first any item to edit",font=['Helvetica',14])

        case "todos":

            window['todo'].update(value=values['todos'][0].strip())
        case "COMPLETE":
            try:
                todo_to_remove = values['todos'][0]
                todolist = functions.get_todolist()

                todolist.remove(todo_to_remove)
                functions.write_todolist(todolist)
                window['todos'].update(values=todolist)
                window['todo'].update(value="")

            except IndexError:
                sg.popup("Please select first any item to Remove", font=['Helvetica', 14])
        case "EXIT":
            break





        case sg.WINDOW_CLOSED:
            break
window.close()

