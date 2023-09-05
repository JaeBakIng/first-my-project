import './App.css';
import React , {useState} from 'react'
import Box1 from './component/Box1';

function App() {
  const [cnt,setCnt] = useState(0);
  const ff=() => {
    setCnt(cnt+1);
    document.title = "클릭횟수" + cnt;
  }


  return (
    <div className="App">
      <div>클릭 횟수 : {cnt}</div>
      <button onClick={ff}>클릭</button>  
      <hr/>
      <hr/>
      <Box1 num = {cnt}/>
      
    </div>
  );
}

export default App;