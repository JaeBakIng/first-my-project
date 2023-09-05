import {useState , useRef , useEffect} from 'react'
import './App.css';

function App() {
  const [cnt , setCnt] = useState(0);
  const cntRef = useRef(0);
  const [render , setRender] = useState(0);

  useEffect(()=>{
    //setRender(render + 1);
    console.log("랜더링" + cntRef.current);
    
  })

  const increaseRef = () =>{
    cntRef.current = cntRef.current + 1;
  }

  const increaseCnt = () => {
    setCnt(cnt + 1);
  }

  return (
    <div className="App">
      <p>state : {cnt}</p>
      <button onClick={increaseCnt}>state</button>
      <p>useRef : {cntRef.current}</p>
      <button onClick={increaseRef}>Ref</button>
    </div>
  );
}

export default App;
