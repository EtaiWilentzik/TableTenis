import logo from './logo.svg';
import './App.css';
import {useState} from "react";

function App() {
    const [count, setCount] = useState(0);
        return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
         dddddd
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
            <br>
            </br>
            count: {count}

        </a>
        <button onClick={() => setCount(count + 1)}>Click me</button>
      </header>
    </div>
  );
}

export default App;
