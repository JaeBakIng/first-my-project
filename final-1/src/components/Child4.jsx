import React from 'react'
import {memo} from 'react'
import {Child3} from './Child3'

const style = {
    height:"200px",
    backgroundColor:"lightgreen",
    padding:"8px",
};


export const Child4 = () => {
  console.log("child4 렌더링")
return (
  <div style={style}>
      <p>Child4</p>
      <Child3/>
  </div> 
)
}
