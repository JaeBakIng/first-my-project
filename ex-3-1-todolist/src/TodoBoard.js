import React from 'react';
import TodoItem from './TodoItem';

function TodoBoard({ todos, handleDelete }) {
  return (
    <div className="TodoBoard">
      {todos.map(todo => (
        <TodoItem key={todo.id} todo={todo} handleDelete={handleDelete} />
      ))}
    </div>
  );
}

export default TodoBoard;