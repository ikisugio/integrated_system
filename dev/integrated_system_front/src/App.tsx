import { useState, useEffect, useContext, useRef } from "react"
import './App.css'
import TestContext from "./main";

function App() {
  const [count, setCount] = useState(0);
  const nameInfo = useContext(TestContext);
  const ref = useRef();

  function handleClick() {
    setCount((prev) => prev + 1);
    console.log(count);
  };

  useEffect(() => {
    console.log("aaa");
  }, [count]);

  const handleRef = () => {
    console.log(ref.current.clientHeight);
  };

  return (
    <div className="App">
      <h1>UseState</h1>
      <button onClick={handleClick}>+</button>
      <p>{count}</p>

      <hr />
      <h1>useContext</h1>
      <p>{nameInfo.name}</p>

      <hr />
      <h1>useRef</h1>
      <input type="text" ref={ref} />
      <button onClick={handleRef}>useRef</button>
    </div>
  )
}

export default App
