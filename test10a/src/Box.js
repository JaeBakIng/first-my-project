import React from 'react'

const Box = (props) => {
    const style={
        backgroundColor:"gold",
        color:"blue",
        width:"50%",
        border:"2px solid black"
    }
  return (
    <div style={style}>
        <p style={{fontSize:"30px"}}>안녕하세요?</p><br/>
        <p style={{fontSize:"20px"}}>{props.name}:{props.count}times clicked!!</p>
    </div>
  )
}

export default Box;