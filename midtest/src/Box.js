import React from 'react'

const Box = (props) => {
    const style = {
        backgroundColor:"gold",
        color:"blue",
        width :"50%",
        border:"2px solid black",
    }
  return (
    <div style={style}>
        <p style={{fontSize:"35px"}}>안녕하세요?</p>
        <p style={{fontSize:"25px"}}>{props.name} : {props.num} times clicked.!</p>
    </div>
    
  )
}

export default Box;