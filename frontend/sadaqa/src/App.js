import React from 'react';
import { BrowserRouter } from 'react-router-dom';
import NavBar from './Components/NavBar/NavBar';
import Footer from './Components/Footer/Footer';
import Router from "./Router/Router";
import './App.css';

function App() {
  return (
    <div className="container App">
      <BrowserRouter>
        <NavBar />
        <div className="container my-5">
          <Router/>
        </div>
        <Footer />
      </BrowserRouter>

    </div>
  );
}

export default App;
