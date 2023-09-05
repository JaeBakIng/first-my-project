import React from 'react'
import {memo} from 'react'

const Child = ({name , age , secname , tellme}) => {
    console.log("자녀 컴포넌트 렌더링")
  return (
    <div style={{border:'2px solid lightblue', padding:'10px'}}>
        <h3>자녀</h3>
        <p>name : {name.myname}</p>
        <p>secname : {secname}</p>
        <p>age : {age}</p>
        <button onClick={tellme}>반가워</button>
        
    </div>
  )
}

export default memo(Child);
//컴포넌트 메모이제이션