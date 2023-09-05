import { useState } from 'react';
import './App.css';
import Pagee from './component/Pagee' 
import {ThemeContext} from './component/context/ThemeContext'
import {UserContext} from './component/context/UserContext'

function App() {


  const [isDark , setIsDark] = useState(false);
  return (
    <UserContext.Provider value = {'사용자'}>
    <ThemeContext.Provider value ={{isDark , setIsDark}}>
      <Pagee/>
    </ThemeContext.Provider>
    </UserContext.Provider>
  );
}

export default App;
