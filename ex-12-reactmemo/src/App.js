import { useState , useMemo, useCallback} from 'react';
import './App.css';
import Child from './components/Child';
function App() {
  const [parentAge , setParentAge] = useState(0);
  const [childAge , setChildAge] = useState(0);

  const increaseParentAge = () => {
    setParentAge(parentAge + 1);
  }

  const increaseChildAge = () => {
    setChildAge(childAge + 1)
  }


  //변수 메모이제이션
  const name = useMemo(()=>{
    return {
      myname : '박민재'
    }
  },[])


  //함수 메모이제이션
  const tellme = useCallback(()=> {
    console.log('방가워 자식들')
  },[])



  console.log('부모 컴포넌트 렌더링')

  return (
    <div style={{border:"2px solid navy" , padding : '10px'}}>
      <h1>부모</h1>
      <p>age: {parentAge}</p>
      <button onClick={increaseParentAge}>부모나이증가</button>
      <button onClick={increaseChildAge}>자식나이증가</button>
      <Child name={name} secname={"박민하"} age={childAge} tellme={tellme}/>
    </div>
  );
}

export default App;
