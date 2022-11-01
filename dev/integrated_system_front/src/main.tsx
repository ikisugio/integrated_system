import React, { createContext } from 'react'
import ReactDOM from 'react-dom/client'
import App from './App'
import './index.css'


const nameInfo = {
  name: "test",
}
const ageInfo = {
  name: "test",
}
const TestContext = createContext(nameInfo)

ReactDOM.createRoot(document.getElementById('root') as HTMLElement).render(
  <TestContext.Provider value={nameInfo}>
    <React.StrictMode>
      <App />
    </React.StrictMode>
  </TestContext.Provider>
)

export default TestContext;