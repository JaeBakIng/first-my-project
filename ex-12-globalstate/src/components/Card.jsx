import {EditButton} from "./EditButton";
import React from 'react'

const style = {
    width:"300px",
    height:"200px",
    margin:"8px",
    borderRadius:"8px",
    backgroundColor:"#e9dbd0",
    display:"flex",
    flexDirection:"column",
    justifiContent:"center",
    alignitems:"center",
}


export const Card = (props) => {
    const {isAdmin} = props;
  return (
    <div style={style}>
        <p>관리자 홍길동</p>
        <EditButton isAdmin={isAdmin}></EditButton>
    </div>
  )
}

