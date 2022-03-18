import React from 'react';
import './App.css';
import {HomePage} from './pages/HomePage';
import {TokenPage} from './pages/TokenPage';
import {MenuPage} from './pages/MenuPage';
import {BackendPage} from './pages/BackendPage';
import {AlgorithmPage} from './pages/AlgorithmPage';
import {ParamsPage} from './pages/ParamsPage';
import {LoadingPage} from './pages/LoadingPage';
import {OutputPage} from './pages/OutputPage';
import {Route, Routes} from 'react-router-dom';

function App() {
  return (
    <div className="App">
      <Routes>
        <Route path='/' element={<HomePage />} />
        <Route path='/token' element={<TokenPage />} />
        <Route path='/menu' element={<MenuPage />} />
        <Route path='/menu/backend' element={<BackendPage />} />
        <Route path='/menu/algorithm' element={<AlgorithmPage />} />
        <Route path='/menu/params' element={<ParamsPage />} />
        <Route path='/menu/loading' element={<LoadingPage />} />
        <Route path='/menu/output' element={<OutputPage />} />
      </Routes>
    </div>
  );
}

export default App;
