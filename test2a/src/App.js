import logo from './logo.svg';
import './App.css';
import aa from './School.png'; // 현재 폴더에있는 school.png를 aa 로 변수를 지정해서 import 함 

function App() {
  const a = "SmartSW학과"

  const ff = (A) => {
    return A;
  }


  return (
    <div className="App">
      <h1 className="SH">연암공과대학교</h1>
      <h3 className="SW">{a}</h3>
      <img src = {aa}/>
      <h4>{ff('LG 연암학원')} 👍</h4>
    </div>          //변수선언 {}
  );
}

export default App;
