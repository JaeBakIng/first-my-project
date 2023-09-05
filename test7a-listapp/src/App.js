import {useState} from 'react'
import './App.css';

function App() {
  const [inputvalue , setinputvalue] = useState("");
  const [list , setlist] = useState([]);
  const [selectItem, setselectItem] = useState(null);
  const [ItemUpdate , setItemUpdate] = useState(false);

  const addlist = () => {
    setlist([...list , inputvalue])
  }

  const dellist = (list , i) => {
    setlist(list.filter((value,index)=> i != index))
  }


  const updateItem = (i) => {
    const newList = [...list]
    newList[i] = inputvalue
    setlist(newList)
    setItemUpdate(false)
    setselectItem(null)
    setinputvalue("")
  }

  function handleUpdateClick(i) {
      setselectItem(list[i]);
      setItemUpdate(true);
    }

  
  
  return (
    <div className="App">
      <h1>간단 메모 애플리케이션</h1>
      <input type='text' value = {inputvalue} onChange={(e)=> {setinputvalue(e.target.value)}}/>
      <button onClick={addlist}>추가</button>
      <hr/>


      <div className = 'AppList'>
      <ul>
        할목록추가
          {
            list.map((item , i)=>{
              return(
              <li key={i}>
                {selectItem && ItemUpdate && selectItem === item ?  (
                  <div>
                  <input
                  type="text"
                  value={inputvalue}
                  onChange={(e) => { setinputvalue(e.target.value) }}/> 

                  <button onClick={updateItem(i)}>수정하기</button>
                </div>
                ) : (<div>{item}</div>)}



                &nbsp;
                <button onClick={() => {handleUpdateClick(i)}}>수정</button> 
                      &nbsp;
                <button onClick={()=>{dellist(list , i)}}>삭제</button>
              </li>

              
              )
            })
          }
      </ul>

      </div>
      
    </div>

    
  );
}

export default App;
