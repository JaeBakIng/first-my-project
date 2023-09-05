import React from 'react'
import {memo} from 'react'

const style = {
    height:"50px",
    backgroundColor:"lightgray",
    border:"2px dashed red"
};
export const Child3 = () => {
    console.log("child3 렌더링")
  return (
    <div style={style}>
        <p>Child3</p>
       
    </div> 
  )
  };

