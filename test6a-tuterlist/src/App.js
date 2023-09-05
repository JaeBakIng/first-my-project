import {useState} from 'react';
import './App.css';

function App() {
  const [list , setList] = useState([]);
  const [inputValue , setinputValue] = useState("");


  const add = () => {
    setList([...list,inputValue])
  }

  const del = (list , i) => {
    setList(list.filter((value,index)=> index != i))
  }

  const alldel = () => {
    setList([])
  }



  return (
    <div className="App">
      <input type='text' value = {inputValue} onChange ={(e) =>{setinputValue(e.target.value)}}/>
      

      <button onClick={add}>추가</button>
      <button onClick={alldel}>전체삭제</button>
      {
        list.map((item,i) => {


            return (
              <div className="todoList">
                {item}
                <button onClick={() => del(list,i)}>삭제</button>
              </div>
            )

            
        })
      }
    

    </div>
  );
}

export default App;
