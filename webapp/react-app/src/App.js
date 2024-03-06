import logo from './logo.svg';
import React, {useState, useEffect} from 'react'
import './App.css';
import {Route, BrowserRouter, Routes, Link} from "react-router-dom"
import Home from "./components/Home"
import Game from './components/Game';

function App() {

  const [game, setGame] = useState("")

  //useEffect runs when the React app is ready to be rendered, putting the array blocks at the end
  //allows it to track certain state variables 
  //fetch gets the /game endpoint from our flask api and uses .then statements to process it as 
  //readible JSON
  // useEffect(() => {
  //   fetch("/api/game").then(result => result.json()).then(data => {
  //     setGame(data[0]["name"])
  //   });
  // }, []);

  return (
    <div>
        <BrowserRouter>
          <Routes>
            <Route exact path='/' element={<Home />} />
            <Route path='/Zelda' element={<Game gamePath={'api/game/zelda'}/>} />
            <Route path='/Mario' element={<Game gamePath={'api/game/mario'}/>} />
          </Routes>
        </BrowserRouter>
    </div>

    //TODO -- GOAL -- Setup two buttons that route to two pages, each returning a different api call --DONE
    //TODO -- GOAL -- Setup a game component system with bootstrap stylings and make a list of those when visiting specific endpoints 
  );
}

export default App;
