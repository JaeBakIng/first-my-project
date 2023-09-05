import React from 'react'

const ColoredMessageCh = (props) => {
    const contentStyle= {
        color : props.color,
        fontSize:"20px"
    }



  return (
    <div>
        <p style={contentStyle}>{props.children}</p>
    </div>
  )
}

export default ColoredMessageCh