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
      const output_result = await fetch(`${API}/get-output`, {
        method: 'GET'
      });
      const getter_result = await fetch(`${API}/get-backend-algorithm-params`, {
        method: 'GET'
      });
      const output_data = await output_result.json();
      console.log('Output:', output_data);
      const getter_data = await getter_result.json();
      setState({...output_data, ...getter_data});
    })();
  }, []);
  const output = (state['err'] ? 'Error: ' : '') + state['output'];
  const imageBase64 = state['err'] ?
      '' : 'data:image/png;base64,' + state['image_base64'];
  const figure_name = 'figure-' + state['backend'] + '-' + state['algorithm'] +
      '-' + state['params'] + '.png';
  return (
    <div>
      <div>
        <h2>Figure:</h2>
        <img src={imageBase64} alt='Figure'></img>
      </div>
      <h3>
        <a download={figure_name} href={imageBase64}>Download figure</a>
      </h3>
      <div>
        <h1>Output: {output}</h1>
      </div>
      <button className='button' id='backBtn' onClick={goToMenu}>
        <span>Back</span>
      </button>
    </div>
  )
}
