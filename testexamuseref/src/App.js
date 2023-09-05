import './App.css';
import { useEffect, useRef, useState } from 'react';

function App() {
  const [msg , setMsg] = useState('');
  const inputRef = useRef();

  const renderRef = useRef(1);
  const [num , setNum] = useState(1);



  const setInputRef = () => {
    const text = inputRef.current.value;
    setMsg(text);
    alert("환영합니다" + text +"님!")
    inputRef.current.focus();
  }

  const numIncrease = () => {
    setNum(num+1);
  }

  useEffect(()=>{
    renderRef.current = renderRef.current + 1
    console.log("랜더링:" ,renderRef.current)
    inputRef.current.focus();
  },[])



  return (
    <div className="App">
      <input ref = {inputRef} placeholder='ID'></input>
      <button onClick={setInputRef}>로그인</button>
      <p>{msg}</p>


      <p>Count :{num}</p>
      <button onClick={numIncrease}>버튼</button>

    </div>
  );
}

export default App;
