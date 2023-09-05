import './App.css';
import Nav from './component/Nav.js'

function Header() {
  return ( <header>
    <h1><a href="/">WEB</a></h1>
  </header>
    
  );
}



function Wel() {
  return( <div>
    <h1>환영!</h1>
    <p>Hello WEB Programing</p>
  </div>


  );
}

function App1() { // react 웹을 보여주는 곳
  return (
    <div className='App'>
    <Header></Header>
    <Nav/>
    <Wel></Wel>
    </div>
  );
}

export default App1;
