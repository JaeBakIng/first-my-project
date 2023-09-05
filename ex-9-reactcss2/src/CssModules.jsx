import classes from "./CssModules.module.scss";
import React from "react";
import { useEffect,useState } from "react";

const CssModules = (props) => {
    var p = document.getElementsByClassName(classes.title);
    var div = document.getElementsByClassName(classes.container);
    useEffect(()=>{
        if(props.num % 2 === 0) {
            div[0].style.backgroundColor = "gold"
            p[0].innerHTML = "22060022" + " cnt = " + props.num
            document.body.style.backgroundColor = "cyan"
        }
        else {
            div[0].style.backgroundColor = "lightpink"
            p[0].innerHTML = "박민재" + " cnt = " + props.num
            document.body.style.backgroundColor = "lightblue"
        }
    })


  return (
    <div id ='div'className={classes.container}>
      <p id='p'className={classes.title}>CSS Modules입니다</p>
      <button onClick={()=>props.setNum(props.num + 1)} className={classes.button}>버튼</button>
    </div>
  );
};

export default CssModules;