import React, { useState, useEffect, useRef } from 'react';

const App = () => {
  const timerRef = useRef(0);
  const [timer, setTimer] = useState(0);

  useEffect(() => {
    timerRef.current = setInterval(() => {
      setTimer((prevTimer) => prevTimer + 1);
    }, 1000);

    return () => {
      clearInterval(timerRef.current);
    };
    
  }, []);



  return (
    <div>
      <h2>타이머: {timer}초</h2>
    </div>
  );
};

export default App;
