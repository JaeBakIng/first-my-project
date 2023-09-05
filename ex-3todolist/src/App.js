import react from 'react'
import { useState } from 'react';
import './App.css';
import TodoBoard from './component/TodoBoard';

function App() {  

  

  const addItem = () => {
    setTodoList([...todoList , inputValue + num]); //2. 입력받은 inputValue를 todoList 배열에 집어넣음
    setNum(num+1)
  };
  
 /* const datadelete = (index) => {// todoList 일부삭제
      todoList.splice(index,1);
      setTodoList([...todoList]);
  }*/

  const datadelete = (index) => {
    setTodoList(todoList.filter((_, i) => i !== index));
  };


  const alldelete = () => {// todoList 전체삭제 
    todoList.splice(0);
     setTodoList([...todoList]);
     
  }

  const clear = () => {
    setTodoList([]);
    setNum(1);
  }

  const cyan = () => {
    document.body.style.backgroundColor = "cyan"
  }

  const red = () => {
    document.body.style.backgroundColor = "red"
  }

  const [inputValue,setInputValue] = useState("");
  const [todoList , setTodoList] = useState([]);
  const [num , setNum] = useState(1);



  return (
    <div className="App">
      <button onClick={cyan}>cyan</button>
      <button onClick={red}>red</button>
      <input type='text' value={inputValue} // 1. 사용자가 입력한 값을 전달받아서 inputValue에 넣음  // onChange -> input 안의 값이 변할때 발생 
        onChange = {(e) => {setInputValue(e.target.value)}}></input> 
      <button onClick={addItem}>할 일 추가</button>
      <button onClick={alldelete}>전체 삭제</button>
      <button onClick={clear}>완전 삭제</button>
      <hr/>
      <h1>오늘의 할 일</h1>



      <TodoBoard todoList={todoList} datadelete = {datadelete}></TodoBoard>
    </div>//todoList변수로 TodoBoard로 보내줌 //datadelete 변수로 datadelete 함수 TodoBoard로 넘겨줌
  );
} // 삭제버튼 만들어서 삭제가 되도록 만들기 

export default App;
