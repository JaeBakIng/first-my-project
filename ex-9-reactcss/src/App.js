import logo from './logo.svg';
import './App.css';

function App() {
  const containerStyle ={
    width:"100%",
    padding:"16px",
    border:"1px solid red",
  }

  const textStyle = {
    color:"blue",
    textAlign:"center"
  }
  return (
    <div style={containerStyle}>
      <p style={textStyle}>Hello World!!</p>
    </div>
  );
}

export default App;
