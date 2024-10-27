import {useState} from "react";

function App() {
    const [message, setMessage] = useState('')

    const getMessage = async () => {
        const response = await fetch('api/')
        const body = await response.json()
        setMessage(body.message)
    }

    return (
        <div className="App">
            {
                message === ''
                ? <button onClick={getMessage}>Try this button!</button>
                : <>Server response was: {message}<button onClick={() => setMessage('')}>reset</button></>
            }
        </div>
    );
}

export default App;
