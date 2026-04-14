import random
import json
import os
from pathlib import Path


def load_from_file():
    path=Path("tasks.json")
    if path.exists() and os.path.getsize(path)>0:
        contents=path.read_text()
        return json.loads(contents)
    else:
        return []
        
task_list=load_from_file()

def add_tasks(task_list):
    task=input("Enter your task")
    new_task={}
    new_task['id']=generate_id(task_list)
    new_task['task']=task
    new_task['status']="NOT_DONE"
    task_list.append(new_task)
    save_to_file(task_list)

def generate_id(task_list):
    while True:
        id=random.randint(1,1000)
        if check_id(id,task_list):
            return id
        
def check_id(id,task_list):
    for task in task_list:
        if task["id"]==id:
            return False
    return True

def list_tasks(task_list):
    id="id" 
    task="task"
    status="status"
    print(f"{id:<10} {task:<25} {status:<20}")
    for task in task_list:
        print(f"{task['id']:<10} {task['task']:<25} {task['status']:<20}")

def update_task(task_list):
    id1=input("enter an id:")
    if id1.isdigit():
        id=int(id1)
        found=False
        for task in task_list:
            if task["id"]==id:
                if task["status"]=="DONE":
                    task["status"]="NOT_DONE" 
                    found=True
                elif task["status"]=="NOT_DONE":
                    task["status"]="DONE"
                    found=True
        if not found:
            print("id not found")
    else:
        print("please print a valid id")
    save_to_file(task_list)

def delete_task(task_list):
    id1=input("enter an id:")
    if id1.isdigit():
        id=int(id1)
        for task in task_list:
            if task["id"]==id:
                task_list.remove(task)
                break
        save_to_file(task_list)

def save_to_file(tasks_list):
    path=Path("tasks.json")
    contents=json.dumps(tasks_list)
    path.write_text(contents)

while True:
    print("1. Add | 2. List | 3. Update | 4. Delete | 5. Exit")
    choice=input("Enter your choice:")
    if choice=="1":
        add_tasks(task_list)
    elif choice=="2":
        list_tasks(task_list)
    elif choice=="3":
        update_task(task_list)
    elif choice=="4":
        delete_task(task_list)
    elif choice=="5":
        print("Thanks for using")
        break
    else:
        print("please enter a correct choice")


            

