import functions
import PySimpleGUI as sg
label=sg.Text("Enter a Todo in list")
input_text=sg.InputText(tooltip="enter any thing")
add_btn=sg.Button("ADD")
window=sg.Window("QAZI's Todo APP",layout=[[label,input_text,add_btn]])
window.read()
window.close()

