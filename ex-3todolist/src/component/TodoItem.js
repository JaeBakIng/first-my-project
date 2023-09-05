import React,{useState} from 'react';

  const TodoItem = (props) => {


    const deleteItem = () => {
      props.datadelete(props.index);
    }

    
    //index값을 받아온 datadelete 함수를 써서 List 지워줌


  return (
    <div className='todo-item'>
          {props.index + 1},{props.item}
          <br></br>
        <button className='delbtn' onClick={deleteItem}>삭제</button> 
    </div>
    
  )
}

export default TodoItem
