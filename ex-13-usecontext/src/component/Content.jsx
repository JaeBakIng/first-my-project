import React, { useContext } from 'react'
import {ThemeContext} from './context/ThemeContext'

const Content = () => {
    const {isDark} = useContext(ThemeContext);
  return (
    <div className='content'
    style={{backgroundColor : isDark ? 'black' : 'white',
            color : isDark ? 'white' : 'black',
            fontWeight:'bolder'}}>
        <h1>박민재 님, 화이팅!</h1>
        
    </div>
  )
}

export default Content