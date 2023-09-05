import React, { useState } from "react";
import './App.css';

function App() {
  const [todos, setTodos] = useState([]);

  function handleAddTodo() {
    const newTodo = // 새로운 todo 아이템을 생성하는 코드;
    setTodos([...todos, newTodo]);
  }

  function handleDelete(index) {
    const newTodos = [...todos];
    newTodos.splice(index, 1);
    setTodos(newTodos);
  }

  return (
      <div>
      <button onClick={handleAddTodo}>Add Todo</button>
      {todos.map((todo, index) => (
        <div key={index}>
          <span>{todo}</span>
          <button onClick={() => handleDelete(index)}>Delete</button>
        </div>
      ))}
    </div>
  );
}
export default App;
