import React from 'react'
import {Child2} from './Child2'
import {memo} from 'react';


const style = {
    height:"200px",
    backgroundColor:"pink",
    padding:"8px",
    width:"30%",
    border:"2px dotted red"
};

export const Child1 = memo((props) => {
    console.log("Child1 렌더링")

    const reset = () => {
      
    }

  return (
    <div style={style}>
        <p>Child1</p>
        <button onClick={props.num}></button>
        <Child2/>
    
    </div>
  )
})

