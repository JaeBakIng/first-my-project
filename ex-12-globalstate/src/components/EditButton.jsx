import React from 'react'

const style = {
    width:"100px",
    padding:"6px",
    borderRadius:"8px",
}

export const EditButton = (props) => {
    const {isAdmin} = props;
  return (
    <div>
        <button style={style} disabled={!isAdmin}>수정</button>
    </div>
  )
}
