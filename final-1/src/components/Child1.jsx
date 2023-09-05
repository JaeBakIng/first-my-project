import React, { useState } from 'react'
import {Child2} from './Child2'
import {memo} from 'react';


const style = {
    height:"200px",
    backgroundColor:"pink",
    padding:"8px",
    width:"30%",
    border:"2px dotted red"
};

export const Child1 = memo(({onClickIncrease , onClickReset}) => {

    console.log("Child1 렌더링")


  return (
    <div style={style}>
        <p>Child1</p>
        <button onClick={onClickIncrease}>리셋</button>
        <Child2/>
    
    </div>
  )
})

