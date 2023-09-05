import {useState} from 'react';
import ColoredMessage from './component/ColoredMessage';
import ColoredMessageCh from './component/ColoredMessageCh';
import './App.css';

function App() {
  const [num,setNum] = useState(0);

  const xx = () => {
    alert("버튼클릭하였네요")
    setNum(num+1);
  }


  return (
    <div className="App">
      <h1 style = {{color:"red"}}>안녕!</h1>
      <ColoredMessage color="blue" messege="잘 지내셩?"/>
      <ColoredMessageCh color="red">잘지내지!</ColoredMessageCh>
      <button onClick={xx}>버튼</button>
      <p>{num}</p>
    </div>
  );
}

export default App;
