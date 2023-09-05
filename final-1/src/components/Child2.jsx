import React, { useState } from 'react'
import {memo} from 'react'

    const style = {
        height:"50px",
        backgroundColor:"lightgray",
        width:"50%",
        border:"2px dashed red"

        
    };
export const Child2 = () => {
    console.log("Child2 랜더링")
  
  return (
    <div style={style}>
  
        <p>Child2</p>
       
    </div>
  )
};

