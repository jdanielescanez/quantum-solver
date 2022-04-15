import React, {useState, useEffect} from 'react';
import {useNavigate} from "react-router-dom";

const API = process.env.REACT_APP_API;

export function OutputPage() {
  const navigate = useNavigate();
  const [state, setState] = useState({
    'algorithm': '',
    'backend': '',
    'params': '',
    'output': '',
    'image_base64': '',
    'err': false
  });
  const goToMenu = () => {
    navigate('/menu', {replace: true});
  }
  useEffect(() => { 
    (async () => {
      const token = window.sessionStorage.getItem('token') || '';
      const output_result = await fetch(`${API}/get-output`, {
        method: 'GET',
        headers: {token}
      });
      const getter_result = await fetch(`${API}/get-backend-algorithm-params`, {
        method: 'GET',
        headers: {token}
      });
      const output_data = await output_result.json();
      console.log('Output:', output_data);
      const getter_data = await getter_result.json();
      setState({...output_data, ...getter_data});
    })();
  }, []);
  const output = (state['err'] ? 'Error: ' : 'Output: ') + state['output'];
  const imageBase64 = state['err'] ?
      '' : 'data:image/png;base64,' + state['image_base64'];
  const figure_name = 'figure-' + state['backend'] + '-' + state['algorithm'] +
      '-' + state['params'] + '.png';
  const copyOutput = () => {
    navigator.clipboard.writeText(output);
    alert('[$] Copied output (' + output + ') to clipboard');
  };
  const showFigure = () => {
    if (!state['err']) {
      return (
        <div>
          <div>
            <h2>Figure:</h2>
            <img src={imageBase64} alt='Figure'></img>
          </div>
          <h3>
            <a download={figure_name} href={imageBase64}>Download figure</a>
          </h3>
        </div>
      );
    }
  };
  const showCopyButton = () => {
    if (!state['err']) {
      return (
        <button className='button' onClick={copyOutput}>Copy output</button>
      );
    }
  };
  return (
    <div>
      {showFigure()}
      <div>
        <h1>{output}</h1>
      </div>
      {showCopyButton()}
      <button className='button' id='backBtn' onClick={goToMenu}>
        <span>Back</span>
      </button>
    </div>
  )
}
