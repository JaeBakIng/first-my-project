import React from 'react'
import Comment from './Comment'

const comments = [{
  name:'세종대왕',
  Comment:'안녕'
},
{
  name:'바이든',
  Comment:'hello'},
{ 
  name:'박민재',
  Comment:'집가고싶다'
}]


const CommentList = () => {
  return (
    <div>
        {
        comments.map ((A) => {  //comments 의 리스트값을 A 매개변수로 받아와서 name 과 Comment 각각 리턴해줌
          return (
            <Comment name={A.name} Comment={A.Comment}></Comment>
          )
        }) 
        
        
        }
    </div>
  )
}

export default CommentList