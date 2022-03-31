import React, {useState, useEffect} from 'react';
import {useNavigate} from "react-router-dom";

const API = process.env.REACT_APP_API;

export function OutputPage() {
  const navigate = useNavigate();
  const [state, setState] = useState({'output': '', 'image_base64': '', 'err': false});
  const goToMenu = () => {
    navigate('/menu', {replace: true});
  }
  useEffect(() => { 
    (async () => {
      const result = await fetch(`${API}/get-output`, {
        method: 'GET'
      });
      const data = await result.json();
      console.log('Output:', data);
      setState(data);
    })();
  }, []);
  const output = (state['err'] ? 'Error: ' : '') + state['output'];
  const imageBase64 = (state['err'] ? '' : 'data:image/png;base64,' + state['image_base64']);
  return (
    <div>
      <div>
        <h2>Figure:</h2>
        <img src={imageBase64} alt='Figure'></img>
      </div>
      <div>
        <h1>Output: {output}</h1>
      </div>
      <button className='button' id='backBtn' onClick={goToMenu}>
        <span>Back</span>
      </button>
    </div>
  )
}
