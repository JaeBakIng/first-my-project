import React, { useContext } from 'react'
import {ThemeContext} from './context/ThemeContext'

const Footer = () => {
    const toggle = () => {
        setIsDark(!isDark);
    }
    const {isDark, setIsDark} = useContext(ThemeContext);
    
  return (
    <div className='footer'
        style={{backgroundColor : isDark ? 'black' : 'lightgray'}}>
        <button className='button' onClick={toggle}>Toggle</button>
    </div>
  )
}

export default Footer