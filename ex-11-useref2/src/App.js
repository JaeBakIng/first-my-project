import { useEffect, useRef, useState } from 'react';
import './App.css';

function App() {
  const inputRef = useRef(0);
  const inputRefname = useRef('');
  
  const [name , setName] = useState('');
  const [namee , setNamee] = useState('');

  const [colorValue , setcolorValue] = useState("black");
  const [colorInputvalue , setcolorInputvalue] = useState("");


  let cntvar = 0;
  const [cnt , setCnt] = useState(0);
  const [render , setRender] = useState(0);
  const cntRef = useRef(0)



  const setcntRef = () => {
    cntRef.current = cntRef.current + 1 // useRef => 랜더링이되면(state가 바뀌면) 값이 바뀜
    console.log("Ref : "+cntRef.current)
  }

  const setCntt = () =>{
    setCnt(cnt+1)

  }

  const setVar = ()=> {
    cntvar += 1;
    console.log("일반변수: "+cntvar)
  }

  /*useEffect(()=>{
    inputRef.current = inputRef.current + 1;
    inputRefname.current = namee;
    console.log("랜더링")
  },[name , namee , cnt])*/

  const changeColor = () =>{
    if(name == "박민재") {
      document.body.style.backgroundColor = "cyan"
      alert("환영합니다 "+name+" 유저님!")
    }
    else{
      alert("아이디가 일치하지 않습니다.")
    }
  }

  const backColor = () => {
    document.body.style.backgroundColor = "white"
  }


  return (
    <div className="App">
      <h1 style={{color:colorValue}}>리액트 과제</h1>

      <p>카운트 횟수 :{cnt}</p>
      <p style={{color:"blue",
                 fontWeight:"bold"}}>Ref : {cntRef.current}</p>
      <button onClick={setCntt}>state</button>
      <button onClick={setcntRef}>Ref</button>
      <hr/>
      <p>일반 변수(cntvar) : {cntvar}</p>
      <button onClick={setVar}>var</button>
      <hr/>

      <input type='text' value={name} onChange={(e)=>{setName(e.target.value)}}></input>
      <button onClick={changeColor}>로그인</button>
      <button onClick={backColor}>색상원위치</button>
      <div>내이름은 {name}</div>
      <div>총 {inputRef.current} 번 렌더링</div>
      <hr/>
      <input type='text' value={namee} onChange={(e)=>{setNamee(e.target.value)}}></input>
      <div>내이름은 {namee}</div>
      <div>변경전 이름은 {inputRefname.current}</div>
      <hr></hr>

      <input placeholder='색상을 입력하세요 (RGB도 가능)' type='text'  value={colorInputvalue} onChange={(e)=> setcolorInputvalue(e.target.value)}></input>
      <button value = {colorInputvalue} onClick={(e)=>{setcolorValue(e.target.value)}} >색상 변경</button>
    </div>
  );
}

export default App;
