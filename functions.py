FilePath = "ful.txt"
def get_todolist(FilePath='ful.txt'):
    with open(FilePath, 'r') as file:
        local_todolist = file.readlines()
    return local_todolist
def write_todolist(listtest,FilePath='ful.txt'):
    with open(FilePath, 'w') as file:
        file.writelines(listtest)