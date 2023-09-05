import React from 'react'

const ColoredMessage = (props) => {
    const contentStyle= {
        color : props.color,
        fontSize:"20px"
    }



  return (
    <div>
        <p style={contentStyle}>{props.messege}</p>
    </div>
  )
}

export default ColoredMessage