import React from 'react'

const Box = (props) => {


  return (

    <div className="Box">

        Hello... xxxx<br/>
        {props.name}:{(props.cnt)} {/* 4, 전달받은 name 과 cnt 를 props라는 매개변수로써 접근지정연산자를 사용하여 씀*/}
       
    </div>
  )
}

export default Box