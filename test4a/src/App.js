import React ,{useState} from 'react';
import './App.css';
import Box from './component/Box.js'; // 1, 컴포넌트를 쓰기위해 Box.js 파일의 경로룰 import해준다





function App() {


  const contentstyle = { // style 객체
    color: "blue",
    fontSize : "20px"
  }





  const [n2,setCnt] = useState(0); //n2를 변수로 지정하여 사용
  const btn1 = () => { // 버튼을 눌렀을때 실행되는 함수
    setCnt(n2+1) //useState 에서 사용하는 함수
    console.log("state 카운트:"+n2);
    alert("카운트 1 추가!");
  }




  return (                       // props 로 name 과 cnt 받아서 props 안에 지정해줌  IOT, {n2}
    <div className="App">

      <button onClick={btn1}>클릭</button>

      <p style={contentstyle}>카운트 {n2}</p> {/*중괄호를 이용하여 n2 변수를 카운트*/}


      <Box name ="AI개론" cnt={n2}></Box> {/* 2, 컴포넌트 반환값으로 위와같은 태그가 아닌 다른 반환되는 파일의 함수를 반환 (아까 import 한 파일)*/}
      <br/>                               {/* 3, 반환하는 과정에서 props라는 매개변수로 name과 cnt를 지정해주어 반환되는 다른파일에 값을전달*/}
      <Box name ="HTML" cnt={n2}/> 
      <br/>
      <Box name ="IOT" cnt={n2}/>
      
      
      
    </div>
  );
}

export default App;
