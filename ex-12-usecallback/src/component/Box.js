import React, { useEffect, useState } from 'react'

const Box = ({BoxStyle}) => {
    const [style , setStyle] = useState({});

    useEffect(()=>{
        console.log("박스 키우기");
        setStyle(BoxStyle());
    },[BoxStyle])

  return (
    <div style={style}></div>
  )
}

export default Box;