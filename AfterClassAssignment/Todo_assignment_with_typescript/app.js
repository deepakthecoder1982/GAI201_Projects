// const uuid = require("uuid");
var todoArray = JSON.parse(localStorage.getItem("todo")) || [];
//for adding todos to the list
var AddTodos = function (title) {
    var newTodo = {
        id: todoArray.length + 1,
        // id:uuidv4(),
        title: title,
        isComplete: false,
    };
    todoArray.push(newTodo);
    // const newTodoArray = [...todoArray,newTodo];
    // console.log(newTodoArray)
    displayTodo(todoArray);
    localStorage.setItem("todo", JSON.stringify(todoArray));
};
var deleteTodo = function (id) {
    var updatedTodos = todoArray.filter(function (task) { return task.id !== id; });
    localStorage.setItem("todo", JSON.stringify(updatedTodos));
    displayTodo(updatedTodos); // Pass the updated array to displayTodo
};
var displayTodo = function (todos) {
    var list = document.getElementById("list_of_todos");
    list.innerHTML = "";
    todos.forEach(function (todo) {
        var listEach = document.createElement("div");
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
        listEach.innerHTML = "\n        <div class=\"flex border\" style=\"display:flex;\">\n        <input type=\"checkbox\"/>\n        <p> ".concat(todo.title, " </p>\n        <p> ").concat(todo.isComplete, "</p>\n        <button>Edit</button>\n        <button onclick=\"deleteTodo(").concat(todo.id, ")\">Delete</button>\n        </div>");
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
var form = document.getElementsByTagName("form")[0];
form.addEventListener("submit", function (e) {
    e.preventDefault();
    var title = document.getElementById("taskInput");
    AddTodos(title.value);
    title.value = "";
});
