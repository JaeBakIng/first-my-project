import React, { useEffect,useState } from 'react'
import './App.css'

const Clock = () => {
    


  const [Clock , setClock] = useState(new Date().toLocaleTimeString())
    useEffect(()=>{
        const timer = setInterval(()=>{
            setClock(new Date().toLocaleTimeString());
        },1000)
    },[])

    

    useEffect(()=>{
        const timer = setInterval(()=>{ 
            console.log("동작중")},1000);

            return (()=>{clearInterval(timer); 
                         console.log("종료");})      

    },[])


  return (
    <div className='Clock'>
        <h1>박민재의 시계</h1>
        <h3>{Clock}</h3>
    </div>
  )
}

export default Clock;