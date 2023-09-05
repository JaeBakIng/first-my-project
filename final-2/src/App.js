
import { useState } from 'react';
import './App.css';
import { useRef } from 'react';

function App() {
  const [num , setNum] = useState(0);
  const Ref = useRef(0)

  const Refincrease = () => {
    Ref.current += 1;
    var result = num + Ref.current;
    console.log("case1 + case2 = "+ result)
  }

  const increase = () =>{
    setNum(num+1);
    console.log("case1 :"+ num)
  }

  return (
    <div className="App">
      <p style={{color:"red",fontWeight:"bolder"}}>case1 클릭: 화면바뀜</p>
      <p style={{color:"red",fontWeight:"bolder"}}>카운트 횟수 : {num}</p>

      <p style={{color:"blue",fontWeight:"bolder"}}>case2 클릭: 화면바뀜</p>
      <p style={{color:"blue",fontWeight:"bolder"}}>case2 클릭:화면 안바뀜</p>
      <p style={{color:"blue",fontWeight:"bolder"}}>카운트 횟수:{Ref.current}</p>
      <button onClick={increase}>case1</button><span>....</span><button onClick={Refincrease}>case2</button>
    </div>
  );
}

export default App;
