import {useState, useEffect } from "react"

const Game = ({gamePath}) => {

    //instead of having setGame to an object, just grab the whole data from the json
    //grab data -- json.map into new array of objects -- set game to be new mapped array
    const [game, setGame] = useState({
        id: null,
        name: null,
        rating: null, 
    })

    //get the game name
    useEffect(() => {
        fetch(gamePath).then(result => result.json()).then(data => {
            setGame({
                id: data[1].id,
                name: data[1].name,
                rating: data[1].rating
             })
        });
    }, []);


    return(
        <div>
            <p>The game name is {game.name}</p>
            <p>The game id is {game.id}</p>
            <p>The game rating is {game.rating}</p>
        </div>

    );
}

export default Game