import React from 'react'

const Clock = () => {
  const time = new Date(); // Date 객체를 만들어서 밑에 h1 태그에 넣어줌
  const hour = time.getHours();
  const minutes = time.getMinutes();
  const seconds = time.getSeconds();

  
  return (
    <div>
    
      <h1>{hour}:{minutes}:{seconds}</h1>

    
    </div>
  )
}

export default Clock