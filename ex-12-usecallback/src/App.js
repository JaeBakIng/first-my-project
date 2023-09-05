import './App.css';
import { useCallback, useState } from 'react';
import Box from './component/Box'

function App() {
  const [size , setSize] = useState(100);
  const [isdark , setIsdark] = useState(true);

  const BoxStyle = useCallback (()=>{
    return {
      backgroundColor : "pink",
      width : `${size}px`,
      height : `${size}px`
      };
  },[size])


  return (
    <div style={{
      background : isdark ? 'white' : 'black',
    }}>

      <input type='number' value={size} onChange={(e)=>setSize(e.target.value)}/>
      <button onClick={()=>setIsdark(!isdark)}>change</button>
      <Box BoxStyle={BoxStyle}/>
    </div>
  );
}

export default App;
