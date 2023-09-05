import React, { useContext } from 'react'
import {ThemeContext} from './context/ThemeContext'
import {UserContext} from './context/UserContext'

const Header = () => {
    const {isDark} = useContext(ThemeContext); 
    // 감싸주면서 선언했던 value를 useContext함수로써 사용
    const user = useContext(UserContext);
  return (
    <div className='header'
    style={{backgroundColor : isDark ? 'black' : 'gray',
            color : isDark ? 'white' : 'red'}}>
        <h1>Welcome {user}!</h1>
        
    </div>
  )
}

export default Header