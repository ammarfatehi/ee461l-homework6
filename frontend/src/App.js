import "./App.css";
import React from "react";

function App() {
  const [name, setName] = React.useState("");
  const [lastname, setLastName] = React.useState("");

  const handleSubmit = () => {
    const url = "/" + name;
    console.log(url);
    fetch(url)
      .then((response) => response.json())
      .then((jsondata) => setLastName(jsondata["payload"]))
      .catch((err) => {
        console.log(err);
      });
  };

  return (
    <div className="App">
      <header className="App-header">
        <p>Enter first name</p>
        <input onChange={(event) => setName(event.target.value)} />
        <button type="button" onClick={handleSubmit}>
          Submit!
        </button>
        <h1>{lastname}</h1>
      </header>
    </div>
  );
}

export default App;
