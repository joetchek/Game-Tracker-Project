import logo from './logo.svg';
import React, {useState, useEffect} from 'react'
import './App.css';

function App() {

  const [game, setGame] = useState("")

  //useEffect runs when the React app is ready to be rendered, putting the array blocks at the end
  //allows it to track certain state variables 
  //fetch gets the /game endpoint from our flask api and uses .then statements to process it as 
  //readible JSON
  useEffect(() => {
    fetch("/game").then(result => result.json()).then(data => {
      setGame(data[0]["name"])
    });
  }, []);

  return (
    <div className='App'>
      <header className='App-header'>
        <p>
          The game name is {game}
        </p>
      </header>
    </div>
  );
}

export default App;
