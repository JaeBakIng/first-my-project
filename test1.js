import React from 'react';
import React, { useState } from 'react';

function Todo() {
  const [task, setTask] = useState('');
  const [list, setList] = useState([]);

  const handleSubmit = (e) => {
    e.preventDefault();
    if (task !== '') {
      setList([...list, task]);
    }
    setTask('');
  };

  const handleDelete = (index) => {
    const temp = [...list];
    temp.splice(index, 1);
    setList(temp);
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <input value={task} onChange={(e) => setTask(e.target.value)} />
        <button type='submit'>Add</button>
      </form>
      <ul>
        {list.map((task, index) => (
          <li key={index}>
            {task}
            <button onClick={() => handleDelete(index)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Todo;


