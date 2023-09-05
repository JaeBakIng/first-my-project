import './App.css';
import CssModules from './CssModules';
import { useState } from 'react';
function App() {
  const [num , setNum] = useState(0);
  return (
    <div>
      <CssModules num={num} setNum = {setNum}/>
    </div>
  );
}

export default App;
