import React from 'react'
import png from './logo.svg';

const Comment = (props) => {
    
    const styles = { // styles 객체를 만듦

        wrapper:{ // wrapper style (제일 바깥 div style)
            margin : 8,
            padding : 8,
            display:'flex',
            flexDirection:'row',
            border : '1px solid red',
            borderRadius:16,
            backgroundColor:'lightgreen',
        },

        imageContainer :{},
            
            image: { //image 의 스타일
                width:50,
                height:75,
                borderRadius:25,
                
            },
        
       

        contentContainer :{ //content의 style (새종대왕 안녕! 의 style)

            margin : 8,
            padding :8,
            display:'flex',
            flexDirection:'column',
            backgroundColor:'pink',


        },


        nameText: { // name{} 의 style
            Color:'black',
            fontSize:16,
            fontWeight:'bold'
        },


        commentText: { // Comment{} 의 style
            Color:'blue',
            fontSize:16
        }
    }
  return (
    <div style={styles.wrapper}> {/*가장큰 div의 style 을 wrapper로함*/} 

        <div style = {styles.imageContainer}> {/*img를 넣기위한 div*/}
            <img src={png} style={styles.image} alt='FFFF'></img> {/*img를 넣고 style을 image 로함 */}
        </div>


        <div style={styles.contentContainer}> {/*코멘트를 넣기위한 div*/}
            <span style={styles.nameText}> {props.name} </span> {/*name*/} {/*props라는 매개변수를 사용하여 세종대왕, 바이든 이라는 문자열을 span 태그에 넣어줌 */}
            <span style={styles.commentText}> {props.Comment} </span> {/*Comment*/} {/*이하동문*/}
        </div>

    </div>



    
  )
}

export default Comment