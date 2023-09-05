import React from 'react'
import TodoItem from './TodoItem'

const TodoBoard = (props) => {



    
  return (
    <div>
        {props.todoList.map((item , index) =>  <TodoItem  item = {item} index = {index} datadelete = {props.datadelete} />)}
    </div>                        //map함수로 index 값을받고                         datadelete 변수로 datadelete함수 TodoItem으로 넘겨줌
  )
}

export default TodoBoard