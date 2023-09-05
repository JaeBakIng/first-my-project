import {useState} from 'react';
import './App.css';

function App() {
  const heavywork = () => {
  console.log('성공')
  return ['트럼프','바이든']
  } 




  const [list,setList] = useState(()=>heavywork());
  const [inputvalue,setInput] = useState("");

  
  const addlist = () => { // 가져온 input값 setName함수로 배열에 넣어줌
    console.log(list)
    setList([...list,inputvalue])
  }

  const dellist = (list , i) => {
    setList(list.filter((value,index) => index != i))

  }


  return (
    <div className="App">
      <input type='text' value={inputvalue} onChange={(e)=>{setInput(e.target.value)}}/> {/* console.log(e.target.value) 타입 text value는 input , InputChange함수로 e(event) 발생하여 input값 가져옴 */}
      <button onClick={addlist}>업로드</button>


      {list.map((item,i) => {//key 값으로 인덱스 받아옴
        return (<div key={i}> 
                  {item}
                  <button onClick={() => dellist(list,i)}>삭제</button>
        </div>
        )
      })}

    </div>
  );
}

export default App;
