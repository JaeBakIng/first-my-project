import React from 'react'
import './App.css';
import Box from './Box';
import {useState,useEffect} from 'react'




function App() {
  const [num , setNum] = useState(0);
  var h1 = document.getElementsByTagName('h1')
  var btn = document.getElementsByTagName('button')
  useEffect(()=>{
    if(num % 2 == 0) {
      document.title = num + "번 클릭!"
      h1[0].style.fontSize = "20px"
      document.body.style.backgroundColor = "pink"
      h1[0].style.color = "red"
      btn[0].style.fontSize = "30px"
    }
    else {
      document.title = num + "번 클릭!"
      document.body.style.backgroundColor = "cyan"
      h1[0].style.fontSize = "40px"
      h1[0].style.color = "red"
      btn[0].style.fontSize = "20px"
    }



  },[num])

  return (
    <div className="App">
     <button onClick={()=>{setNum(num+1)}}>{num % 2 ==0 ? `짝수 ${num}`:`홀수 ${num}`}</button>
     <h1>{num}번 클릭!</h1>
     <Box name='박민재' num={num}/>
    </div>
  );
}

export default App;
