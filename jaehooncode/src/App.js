import './App.css';
import React, {useState} from 'react'
import List from './List.js';
//TODOLIST 를 코드 보지 않고 만들어 보자
//댓글창을 컴포넌트 구조로 만들어 보자

 
function App() {
  const [inputText, setInputText] = useState('')//빈 문자열값으로 초기화
  const [list, setList] = useState([])// 빈 배열을 생성, inputtext의 값이 여기로 들어감 

  const addItem =()=>{
    setList([...list, inputText]);
  }

  const delItem = (list , i) => {
    setList(list.filter((value,index) => index != i))
  }


//입력창 잇어야 하고, 전송 버튼

  return (
    <div className="App">
      <h1>To do list</h1>
      <input type="text" onChange={(e)=> setInputText(e.target.value)}></input>
      <button onClick={addItem}>전송</button>
      <h2>오늘의 할일 </h2>
      <hr/>
      
      <List list={list} delItem={delItem}></List>
    </div>
  );
}
export default App; 