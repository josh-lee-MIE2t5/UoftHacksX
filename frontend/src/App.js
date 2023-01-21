import logo from "./logo.svg";
import "./App.css";
// import { useState } from "react";

// const eventItems = [
//   {
//     _id: 1,
//     title: "UoftHacksx",
//     description: "death",
//     location: "my hall",
//     _type: "competition",
//     startDate: Date.now(),
//     endDate: Date.now(),
//     registrationReq: false,
//     frequency: "one time",
//   },
// ];

function App(props) {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
