import React from 'react';

function TodoItem({ todo, handleDelete }) {
  const handleClick = () => {
    handleDelete(todo.id);
  };

  return (
    <div className="TodoItem">
      <span>{todo.text}</span>
      <button onClick={handleClick}>삭제</button>
    </div>
  );
}

export default TodoItem;