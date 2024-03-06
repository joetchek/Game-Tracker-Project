import {Link} from "react-router-dom"

const Home = () => {
    return (
        <>
            <p className="lead">
                This is the home page for the Game Tracker Project
            </p>

            <Link to="/Mario">
                <button type="button" class="btn btn-primary">Mario</button>
            </Link>
            <Link to="/Zelda">
                <button type="button" class="btn btn-secondary">Zelda</button>
            </Link>
        </>
    );

};

export default Home