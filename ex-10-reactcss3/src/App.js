import './App.css';
import { StyledComponents } from './components/StyledComponents';
import { Emotion } from './components/Emotion';
import { StyledJsx } from './components/StyledJsx';
import { TailwindCss } from './components/TailwindCss';

function App() {
  return (
    <div className="App">
      <StyledJsx/>
      <StyledComponents/>
      <Emotion/>
      <TailwindCss/>
    </div>
  );
}

export default App;
