import React from 'react';
import {HomePage} from './pages/HomePage';
import {TokenPage} from './pages/TokenPage';
import {MenuPage} from './pages/MenuPage';
import {BackendPage} from './pages/BackendPage';
import {AlgorithmPage} from './pages/AlgorithmPage';
import {ParamPage} from './pages/ParamPage';
import {LoadingPage} from './pages/LoadingPage';
import {OutputPage} from './pages/OutputPage';
import {LoadingExperimentPage} from './pages/LoadingExperimentPage';
import {Route, Routes} from 'react-router-dom';
import './App.css';

function App() {
  return (
    <div className="App">
      <div id='bg-image'></div>
      <div id='triangle'></div>
      <div id='triangle2'></div>
      <Routes>
        <Route path='/' element={<HomePage />} />
        <Route path='/token' element={<TokenPage />} />
        <Route path='/menu' element={<MenuPage />} />
        <Route path='/menu/backend' element={<BackendPage />} />
        <Route path='/menu/algorithm' element={<AlgorithmPage />} />
        <Route path='/menu/param' element={<ParamPage />} />
        <Route path='/menu/loading' element={<LoadingPage />} />
        <Route path='/menu/loading-experiment' element={<LoadingExperimentPage />} />
        <Route path='/menu/output' element={<OutputPage />} />
      </Routes>
    </div>
  );
}

export default App;
