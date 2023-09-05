import React, { useEffect, useState } from 'react'

const Counter = (props) => {
    const [num , setNum] = useState(0);
    const [count , setCount] = useState(0);

    useEffect(()=> {
        if(count %2 ==0) {
            document.title = `총 ${count}번클릭`
            document.body.style.backgroundColor = 'gold'
            document.body.style.fontWeight='bold'
            document.body.style.fontSize ='25px'
            document.body.style.color = 'blue'
        }
        else {
            document.title = 'ㅎㅇ'
            document.body.style.fontWeight='light'
            document.body.style.fontSize ='15px'
            document.body.style.color = 'red'
        }
    })
    
   // const btn_1 = () => {
     //   setNum(num+1);
    //}

  return (
    <div>
        <p>{count}번 클릭했습니다. {props.name}</p>
        <button onClick={() => {setNum(num+1)}}>클릭</button>
        <button onClick={() => {setCount(count+1)}}>타이틀</button>
    </div>
  )
}

export default Counter