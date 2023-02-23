#from functions import get_todos,write_todos   
import functions
import time

now=time.strftime("%b %d,%Y %H:%M:%S")
print ("It is", now)
while True: 
    user_action=input("Type add,show,edit ,complete or exit: ")
    user_action=user_action.strip()
    if user_action.startswith('add'):
        #Why no print line by line?
        todo=user_action[4:]
        todos=functions.get_todos()
        todos.append(todo + '\n')           
        functions.write_todos(todos)
    #Codigo para mostrar listado
    elif user_action.startswith('show'):
         todos=functions.get_todos()
         newTodos=[]
         for i in todos:
            newItem=i.strip("\n")
            newTodos.append(newItem)

         for index,item in enumerate(newTodos):
            print (index+1,'-',item)


    elif user_action.startswith('edit'): 
        try:
            number=int(user_action[5:])            
            todos=functions.get_todos()
            existing_todo=todos[number-1]
            print('Here is todos existing',todos)
            todos[number-1]=input(f"Vas a editar el valor {existing_todo} Ingrese el nuevo valor todo AJUA: ")+'\n'
            functions.write_todos()
        except ValueError:
            print("Your command is not valid")
            continue
        
    elif user_action.startswith('complete'):
        try:
            todos=functions.get_todos()
            number=int(user_action[9:])
            todo_to_remove=todos[number-1]
            todos.pop(number-1)                
            todos.remove(todo_to_remove)

            functions.write_todos()
            print(f"Todo {todo_to_remove} was removed from the list.")
        except IndexError:
            print("There is no item with that number")
            continue

    elif 'exit' in user_action:
        break
    else:
        print("Command is not valid")
print("Bye")