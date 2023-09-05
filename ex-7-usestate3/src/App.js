import {useEffect, useState} from 'react'
import Clock from './Clock';
import './App.css';

function App() {
  const [cnt , setCnt] = useState(0);
  const [inputvalue , setinputValue] = useState('');
  const[time , setTime] = useState(false);


  useEffect(()=>{
    console.log("렌더링")
  },[cnt])



  return (
    <div className="App">
      <button onClick={()=> {setCnt(cnt + 1)}}>업데이트</button> <span>카운트 : {cnt}</span>
      <hr/>
      <input type='text' value={inputvalue} onChange={(e)=>{setinputValue(e.target.value)}}></input>
      <p>이름: {inputvalue}</p>
      <hr></hr>
      {time && <Clock/>}
      <button onClick={()=>{setTime(!time)}}>Toggle Timer</button>
    </div>
  );
}

export default App;
