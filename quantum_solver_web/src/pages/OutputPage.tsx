import React, {useState, useEffect} from 'react';
import {useNavigate} from "react-router-dom";

const API = process.env.REACT_APP_API;

export function OutputPage() {
  const navigate = useNavigate();
  const [state, setState] = useState({'output': '', 'err': false});
  const goToMenu = () => {
    navigate('/menu', {replace: true});
  }
  useEffect(() => { 
    (async () => {
      const result = await fetch(`${API}/get-output`, {
        method: 'GET'
      });
      const data = await result.json();
      setState(data);
    })();
  }, []);
  const output = (state['err'] ? 'Error: ' : '') + state['output'];
  return (
    <div>
      <h1>Output</h1>
      <h3>{output}</h3>
      <button className='button' id='backBtn' onClick={goToMenu}>
        <span>Back</span>
      </button>
    </div>
  )
}
