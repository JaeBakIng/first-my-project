import React, { useState } from 'react';
import TodoBoard from './TodoBoard';

function App() {
  const [todos, setTodos] = useState([
    { id: 1, text: '항목 1' },
    { id: 2, text: '항목 2' },
    { id: 3, text: '항목 3' }
  ]);

  const handleDelete = (id) => {
    const updatedTodos = todos.filter(todo => todo.id !== id);
    setTodos(updatedTodos);
  };

  return (
    <div className="App">
      <h1>TodoList</h1>
      <TodoBoard todos={todos} handleDelete={handleDelete} />
    </div>
  );
}

export default App;