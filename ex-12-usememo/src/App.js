import './App.css';
import { useMemo, useState } from 'react';

function App() {
  const [hNum , sethNum] = useState(0);
  const [eNum , seteNum] = useState(0);

  const hplus = (num) => {
    console.log("어려운계산")
    for(let i = 0; i<=999999; i++) {}
    return hNum + 10000;
  }
  const hardplus = useMemo(()=>{return hplus(hNum)},[hNum]) 

  const eplus = (num) =>{
    console.log('쉬운계산')
    return eNum + 1;
  }

  const easyplus = eplus(eNum);




  return (
    <div className="App">
        <h3>어려운 계산기</h3>
        <input type = 'number' value={hNum} onChange={(e)=>(sethNum(parseInt(e.target.value)))}></input>
        <span>+10000 = {hardplus}</span><hr/>

        <h3>쉬운 계산기</h3>
        <input type = 'number' value={eNum} onChange={(e)=>(seteNum(parseInt(e.target.value)))}></input>
        <span>+1 = {easyplus}</span><hr/>
    </div>
  );
}

export default App;
