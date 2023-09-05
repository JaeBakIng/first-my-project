import './App.css';
import { useState } from 'react';
import {Card} from './components/Card'

export default function App () {
  const [isAdmin , setisAdmin] = useState(false);

  const onClickSwitch = () => setisAdmin(!isAdmin);

  return (
    <div className="App">
      {isAdmin ? <span>관리자입니다.</span> : <span>관리자가 아닙니다.</span>}
      <button onClick={onClickSwitch}>전환</button>
      <Card isAdmin ={isAdmin}/>
    </div>
  );
}


