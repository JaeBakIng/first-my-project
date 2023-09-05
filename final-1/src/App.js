import React from "react";
import { useState,useCallback } from "react";
import {Child1} from "./components/Child1";
import {Child4} from "./components/Child4";
import './App.css';

export const App = () => {
  const [num , setNum] = useState(0);
  const [renum , setreNum] = useState(0);
  
  const onClickbutton = useCallback(() => {
    setNum(num+1);
  },[num])
  
  const onClickIncrease = useCallback(()=>{
    setreNum(renum+1);
    setNum(0);
  },[renum])

  console.log("App 랜더링")

  return (
    <div className="App">
      <button onClick = {onClickbutton}>클릭</button>
      <p>{num}</p>
      <p>리셋 횟수 : {renum}</p>
      <Child1 onClickIncrease={onClickIncrease}/>
      <Child4/>
    </div>
  );
}
