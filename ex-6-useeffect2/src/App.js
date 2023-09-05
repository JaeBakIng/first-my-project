import { useEffect, useState } from 'react';
import './App.css';

function App() {
  const [num1 , setNum1] = useState(0);
  const [num2 , setNum2] = useState(0);
  const [cnt1 , setCnt] = useState(0);
  const [text , setText] = useState("");
  const [color , setColor] = useState("cyan");

  const cnt = () => {
    setNum1(num1 + 1);
  }

  useEffect(()=> {
    console.log(num1 + ":" + num2 + ":"+ color)
    setText(color);
  },[num1 , num2 ,color , cnt1])


 

  const changeColor = () => {
    setCnt(cnt1 + 1);
    if(cnt1 % 3 == 0) {
      setColor("gray")
    }
    else if (cnt1 % 2 == 0) {
      setColor("black")
    }
    else {
      setColor("gold")
    }
  }

  


  return (
    <div className="App">
      <h2>useEffect 실습</h2>
      <p style={{color : color,}}>{text}</p>

      <div
      style={{
        width: "200px",
        height: "100px",
        border: "2px dotted black",
        backgroundColor: color,
      }}>

      </div>
      <div>
      <button onClick={()=>setColor("blue") + setText(color)}>파랑</button>
      <button onClick={()=>setColor("red")+ setText(color)}>빨강</button>
      <button onClick={()=>setColor("pink")+setText(color)}>분홍</button>
      <button onClick={()=>setColor("green")+setText(color)}>녹색</button>
      <button onClick={()=>setColor("orange")+setText(color)}>주황</button>
      </div>
      <hr/>
      <button onClick={cnt}>카운트1</button>
      <button onClick={()=> setNum2(num2+1)}>카운트2</button>
      <button onClick={changeColor}>색상변경</button>

    </div>
  );
}

export default App;
