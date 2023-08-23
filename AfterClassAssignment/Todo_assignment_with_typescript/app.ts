// const uuid = require("uuid");

// import { v4 as uuidv4 } from "uuid";
interface todo {
  id: Number;
  title: String;
  isComplete: boolean;
}

const todoArray: todo[] = JSON.parse(localStorage.getItem("todo")) || [];

//for adding todos to the list
const AddTodos = (title: string) => {
  
  const newTodo: todo = {
    id: todoArray.length + 1,
    // id:uuidv4(),
    title,
    isComplete: false,
  };
  todoArray.push(newTodo)
  // const newTodoArray = [...todoArray,newTodo];
// console.log(newTodoArray)
  displayTodo(todoArray);
  localStorage.setItem("todo",JSON.stringify(todoArray));

};


const deleteTodo = (id: number) => {
  const updatedTodos = todoArray.filter((task) => task.id !== id);
  localStorage.setItem("todo", JSON.stringify(updatedTodos));
  displayTodo(updatedTodos); // Pass the updated array to displayTodo
};

const displayTodo = (todos: todo[]) => {
  const list = document.getElementById("list_of_todos");
  list.innerHTML = "";
  todos.forEach((todo) => {
    const listEach = document.createElement("div");
    // let mainDiv = document.createElement("div");
    // let input = document.createElement("input");
    // input.setAttribute("type", "checkbox");
    // let title = document.createElement("p").innerText = `${todo.title}`;
    // // title.innerText = todo.title;
    // let status = document.createElement("p").innerText = `${todo.isComplete}`;;
    // // title.innerText = todo.status;
    // let Edit = document.createElement("button").innerText = "Edit";
    // let Delete = document.createElement("button").innerText = "Delete";;
    
    // listEach.append(input,title,status,Edit,Delete);
    // list.append(listEach)
    listEach.innerHTML = `
        <div class="flex border" style="display:flex;">
        <input type="checkbox"/>
        <p> ${todo.title} </p>
        <p> ${todo.isComplete}</p>
        <button>Edit</button>
        <button onclick="deleteTodo(${todo.id})">Delete</button>
        </div>`;
        list.append(listEach);
    });
};

displayTodo(todoArray);
// for deleting from the list

// function deleteTask(taskId: number) {
//     const taskIndex = todoArray.findIndex(task => task.id === taskId);
//     if (taskIndex !== -1) {
//         tasks.splice(taskIndex, 1);
//     }
// }



const form = document.getElementsByTagName("form")[0] as HTMLFormElement;
form.addEventListener("submit", (e) => {
  e.preventDefault();
  const title = document.getElementById("taskInput") as HTMLInputElement;
  AddTodos(title.value);
  title.value = "";
});
