import {useState, useEffect } from "react"

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
                rating: object.rating
            }));
            console.log(newData)
            setGameData(newData)
        });
    }, []);

    //make the games return a game component for each of these next
    return(
        <div>
            {gameData.map(game => (
                <p>
                    <li>
                        <p>The games id is {game.id}</p>
                        <p>The games name is {game.name}</p>
                        <p>The games rating is {game.rating}</p>
                    </li>
                </p>
            ))}
        </div>
    );
}

export default Game