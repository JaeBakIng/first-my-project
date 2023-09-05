import { useState , useRef , useEffect} from 'react';
import './App.css';

function App() {
  let cntvar = 0;
  const [cnt , setCnt] = useState(0);
  const [render , setRender] = useState(0);
  const cntRef = useRef(0);


  useEffect(()=>{
    console.log("랜더링")
    setRender(render+1)
  },[cnt])



  const setcntRef = () => {
    cntRef.current = cntRef.current + 1 // useRef => 랜더링이되면(state가 바뀌면) 값이 바뀜
    console.log("Ref : "+cntRef.current)
  }

  const setCntt = () =>{
    setCnt(cnt+1)
    console.log("state click!")

  }

  const setVar = ()=> {
    cntvar += 1;
    console.log("일반변수: "+cntvar)
  }



  return (
    <div className="App">
      <p>카운트 횟수 :{cnt}</p>
      <p style={{color:"blue",
                 fontWeight:"bold"}}>Ref : {cntRef.current}</p>
      <button onClick={setCntt}>state</button>
      <button onClick={setcntRef}>Ref</button>
      <hr/>
      <p>일반 변수(cntvar) : {cntvar}</p>
      <button onClick={setVar}>var</button>
    </div>
  );
}

export default App;
