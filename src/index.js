import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import 'bootstrap/dist/css/bootstrap.min.css';
import {BrowserRouter as Router,Route,
  Redirect,Switch} from 'react-router-dom';
import PCOSQuiz from './components/quiz_start';


function Routes(){
    return(
      <Router>
        <div>
          <Switch>
          <Route path="/quiz" component = {PCOSQuiz} />
          </Switch>
        </div>
      </Router>
    )
}

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
