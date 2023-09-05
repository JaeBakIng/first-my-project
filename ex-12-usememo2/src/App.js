import { useEffect, useState, useMemo } from 'react';
import './App.css';

function App() {
  const [num , setNum] = useState(0);
  const[isKorea , setIskorea] = useState(true);
  //const location = isKorea ? '한국' : '미국'; //원시타입 -> 숫자,문자열,불리언,null값 등등

  const location = useMemo(()=>{
    return{country : isKorea ? '한국' : '미국'}
  },[isKorea])

  useEffect(()=>{ 
    console.log('useEffect호출')
  },[location]) // object타입이면 주소가 저장되기때문에 계속 렌더링이 됨.


  return (
    <div className="App">
      <h2>1일 식사횟수</h2>
      <input type='number' value={num} onChange={(e)=>{setNum(e.target.value)}}/>
      <hr/>
      <h2>한국에 있니? 미국에 있니?</h2>
      <p>장소 : {location.country}</p>
      <button onClick={()=>setIskorea(!isKorea)}>Toggle</button>
    </div>
  );
}

export default App;
