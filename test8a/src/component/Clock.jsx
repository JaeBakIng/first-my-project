import React from 'react'



const Clock = () => {
    const time = new Date();
    const hour = time.getHours();
    const min = time.getMinutes();
    const sec = time.getSeconds();
    return (
    <div>
    <h1>{hour}:{min}:{sec}</h1>
    </div>
  )
}

export default Clock;