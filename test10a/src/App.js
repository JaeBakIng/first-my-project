import React from'react';
import {useState,useEffect} from 'react';
import Box from './Box';


function App() {
  const[count,setCount]=useState(0);
  var h1=document.getElementsByTagName('h1');
  const name="박민재";
  useEffect(()=>{
    if(count%2===0){
       document.title={count}+"번 클릭!!";
      document.body.style.backgroundColor='pink';
      h1[0].style.fontSize='20px';
    }
    else {
      document.title={count}+"번 클릭!!";
      document.body.style.backgroundColor='cyan';
      h1[0].style.fontSize='40px';
          }
  },[count])
  return (
    <div className="App">
      
      <button onClick={()=>setCount(count+1)}> {count % 2 ==0 ? `짝수${count}`:`홀수${count}`} </button>
      <h1>{count}번 클릭!</h1>
     <Box name={name} count={count}/>
    </div>
  );
}

export default App;