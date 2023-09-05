import DatePicker from "react-datepicker";
import "react-datepicker/dist/react-datepicker.css";
import Clock from './component/Clock';
import './App.css';
import React from 'react';
import { useState } from 'react';
import { useEffect } from 'react';

function App() {
  const [cnt, setCnt] = useState(0);

  const [inputvalue, setInputvalue] = useState("");
  const [todos, setTodos] = useState({});

  const [selectedDate, setSelectedDate] = useState(""); // 날짜를 바꾸는 state

  const [updateInputvalue, setUpdateInputvalue] = useState("");
  const [updateIndex, setUpdateIndex] = useState(-1); // 수정할 항목의 인덱스 저장

  const [colorValue, setcolorValue] = useState("black"); // 색상을 바꾸는 usestate
  const [colorInputvalue, setcolorInputvalue] = useState("");

  useEffect(() => {
    setCnt(cnt + 1);
    document.title = `useEffect 함수 ${cnt}번 실행`;
    console.log("list 작업 완료");
  }, [todos]);

  const addTodo = () => {
    if (!selectedDate) {
      alert("날짜를 선택하세요.");
      return;
    }

    const newTodos = { ...todos };
    if (!newTodos[selectedDate]) {
      newTodos[selectedDate] = [];
    }
    
    newTodos[selectedDate].push({ task: inputvalue, completed: false });
    setInputvalue("");
    setTodos(newTodos);
  };

  const delTodo = (date, i) => {
    const newTodos = { ...todos };
    newTodos[date].splice(i, 1);
    if (newTodos[date].length === 0) {
      delete newTodos[date];
    }
    setTodos(newTodos);
  };

  const updateTodo = (date, i) => {
    setUpdateIndex(i);
    setUpdateInputvalue(todos[date][i].task);
  };

  const toggleComplete = (date, i) => {
    const newTodos = { ...todos };
    newTodos[date][i].completed = !newTodos[date][i].completed;
    setTodos(newTodos);
  };

  const handleDateChange = (date) => {
    setSelectedDate(date);
  };

  return (
    <div className="App">
      <Clock />


      {/*색상을 변경하는 코드*/}
      <input
        placeholder="색상을 입력하세요 (RGB도 가능)"
        type="text"
        value={colorInputvalue}
        onChange={(e) => setcolorInputvalue(e.target.value)}
      ></input>
      <button
        value={colorInputvalue}
        onClick={(e) => {
          setcolorValue(e.target.value);
        }}
      >
        색상 변경
      </button>
        


      <h1 style={{ color: colorValue }}>오늘의 할 일</h1>

      <div style={{ display: "flex", alignItems: "center" }}>
        <DatePicker
          locale="ko"
          selected={selectedDate}
          onChange={handleDateChange}
          placeholderText="날짜 선택"
          popperPlacement="auto"
         />
         
      </div>
      

       <input
        type="text"
        value={inputvalue}
        placeholder="할 일을 추가하세요"
        onChange={(e) => {
          setInputvalue(e.target.value);
        }}
      ></input>
      <button onClick={addTodo}>추가</button>

     

      {selectedDate && todos[selectedDate] && todos[selectedDate].length > 0 ? (
        todos[selectedDate].map((item, i) => (
          <div key={i}>
            {updateIndex === i ? (//updateIndex가 key값이 서로 같지 않으므로 수정버튼을 누름으로써 true 로 변경하고 true안 코드 실행
              <div>
                <input
                  type="text"
                  value={updateInputvalue}
                  onChange={(e) => setUpdateInputvalue(e.target.value)}
                ></input>
                <button
                  onClick={() => {
                    const newTodos = { ...todos };
                    newTodos[selectedDate][i].task = updateInputvalue;
                    setTodos(newTodos);
                    setUpdateIndex(-1);
                  }}
                >
                  완료
                </button>
                  {/*수정할 list의 인댁스값을 가져와서 수정할 updateInputvalue 를 list에 저장하고 -1로 초기화 함으로써 편집을 종료*/}
              </div>
            ) : (
              <>
                <input
                  type="checkbox"
                  checked={item.completed}
                  onChange={() => toggleComplete(selectedDate, i)}
                />
                <span
                  className="list-item"
                  style={{ display: "inline-block" }}
                >
                  {item.task}
                </span>
                <button
                  onClick={() => updateTodo(selectedDate, i)}
                  style={{ display: "inline-block" }}
                >
                  수정
                </button>
                <button
                  onClick={() => delTodo(selectedDate, i)}
                  style={{ display: "inline-block" }}
                >
                  삭제
                </button>
              </>
            )}
          </div>
        ))
      ) : (
        <div>할 일이 없습니다.</div>
      )}
    </div>
  );
}

export default App;