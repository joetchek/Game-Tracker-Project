import {useState, useEffect } from "react"
import GameComponent from "./GameComponent";

function round(value, decimal) {
    return value.toPrecision(decimal);
}

const Game = ({gamePath}) => {

    //instead of having setGame to an object, just grab the whole data from the json
    //grab data -- json.map into new array of objects -- set game to be new mapped array --DONE
    const [gameData, setGameData] = useState([])

    //get the game name
    useEffect(() => {
        fetch(gamePath).then(result => result.json()).then(data => {
            //console.log(data)
            //creating a JS object here so use the brackets inside the parenthesis
            const newData = data.map(object => ({
                id: object.id,
                name: object.name,
                rating: round(object.rating, 4)
            }));
            console.log(newData)
            setGameData(newData)
        });
    }, []);

    //make the games return a game component for each of these next
    return(
        <div>
            {gameData.map(game => ( 
                <GameComponent 
                    name={game.name} 
                    id={game.id} 
                    rating={game.rating} 
                />
            ))}
        </div>
    );
}

export default Game