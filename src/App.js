import logo from './logo.svg';
import Button from 'react-bootstrap/Button';
import './App.css';
import { useHistory } from 'react-router-dom';


function App() {
  const history = useHistory();
  function handleClick() {
    history.push("/quiz");
  }
  return (
    <div className="App">
      <header className="App-header">
       
        <p>
         Get to know yourself better
        </p>
      <Button onClick={handleClick}className="class" variant="light" size="lg">
   <h2> Detect now</h2>
  </Button>
        
      </header>

      <a href="https://imgur.com/LfNNzXK"><img src="https://i.imgur.com/LfNNzXK.png" alt="block"/></a>
    </div>
  );
}

export default App;
