import {useState} from 'react';
import './App.css';

function App() {
  const [num,setNum] = useState(0);

  


  const bcolor = () => {
    document.body.style.backgroundColor = "cyan"
  }
  
  const btn = () => {
    setNum(num+1)
    if (num % 2 != 0) {
      document.body.style.backgroundColor = "red"
    }
    else {
      document.body.style.backgroundColor = "blue"
    }
  }
  
  const btnM = () => {
    setNum(num-1)
  }

  const btnZ = () => {
    setNum(0)
    document.body.style.backgroundColor = "white"
  }

  
  return (
    <div className="App">
    <p>{num}</p>
    <button onClick={btn}>증가</button>
    <button onClick={btnM}>감소</button>
    <button onClick={btnZ}>리셋</button>
    <button onClick={bcolor}>바탕색변경</button>
    </div>
  );
}

export default App;
