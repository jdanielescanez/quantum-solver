// reacts imports
// import React from 'react';
import {
  BrowserRouter as Router,
} from 'react-router-dom'
import { CssBaseline, ThemeProvider } from '@mui/material';
import { useSelector } from 'react-redux';

// Mui imports
import Box from '@mui/material/Box';


import PrincipalContainer from './PrincipalContainer';


function App() {
  const Theme = useSelector((state: any) => state.theme_mode_reducer.Theme);
  return (
    <ThemeProvider theme={Theme}>
      <Box sx={{ display: 'flex' }}>
        <Router>
          <CssBaseline />
          <PrincipalContainer />
        </Router>
      </Box>
    </ThemeProvider>
  );
}

export default App;