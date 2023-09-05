import './App.css';
import { useState } from 'react';
import { useEffect } from 'react';

function App() {
  const color = ["red","blue","green"]
  const [setColor , setbgColor] = useState("pink");
  const [colorIndex , setColorIndex] = useState(0);
  const [stop , setStop] = useState(false);

  const [wvalue , setwValue] = useState(0);
  const [hvalue , sethValue] = useState(0);

  const [Wwvalue , setWwValue] = useState(1);
  const [Hhvalue , setHhValue] = useState(1);
  
  const changeWvalue= () => {
    setWwValue((e)=> e = wvalue)
  }

  const changeHvalue= () => {
    setHhValue((e)=> e = hvalue)
  }
  

  const setchangeColor = ()=> {
    setStop(true);
  }

  const setstopColor = () => {
    setStop(false)
  }

  useEffect(()=> {
    let interval;
    if(stop) {
      interval = setInterval(()=>{
        setColorIndex((colorIndex + 1) % color.length)
      },1000)
    }
    return () => clearInterval(interval); //해당 컴포넌트가 unmount될때 clearInterval 함수 실행..
  },[colorIndex , stop]);
  

  useEffect(()=>{
    setbgColor(color[colorIndex])
  },[colorIndex])

  return (
    <div className="App">
      <input type ='number' value={wvalue} onChange={(e)=>{setwValue(e.target.value)}}></input>
      <button onClick={changeWvalue}>가로 길이</button>
      <br/>
      <input type ='number' value={hvalue} onChange={(e)=>{sethValue(e.target.value)}}></input>
      <button onClick={changeHvalue}>세로 길이</button>
      <div style={{backgroundColor : setColor , width: Wwvalue+"px" , height : Hhvalue+"px"}} className="div1">
      </div>
      <button onClick={() => setchangeColor()}>시작</button>
      <button onClick={() => setstopColor()}>종료</button>


      
    </div>
  );
}

export default App;




