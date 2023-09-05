import React from 'react'
import App from './App'

const List = (props) => {

    

    const style = {
        border:"2px solid red"
    }


  return (
    props.list.map((item,i)=> {
        return (
            <div style={style}>
                {item} <button onClick={() => props.delItem(props.list,i)}>삭제</button>
            </div>
        )
    })
  )
}

export default List