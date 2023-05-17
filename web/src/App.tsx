// reacts imports
// import React from 'react';
import {
  BrowserRouter as Router,
} from 'react-router-dom'
import { CssBaseline, ThemeProvider } from '@mui/material';
import { useSelector } from 'react-redux';

// Mui imports
import Box from '@mui/material/Box';

import { ColorModeContext, useMode } from './Redux/reducers/ThemeFunctions/CustomTheme';

import PrincipalContainer from './PrincipalContainer';


function App() {
  const [theme, colorMode] = useMode();

  return (
    <ColorModeContext.Provider value={colorMode}>
      <ThemeProvider theme={theme}>
        <Box sx={{ display: 'flex' }}>
          <Router>
            <CssBaseline />
            <PrincipalContainer />
          </Router>
        </Box>
      </ThemeProvider>
    </ColorModeContext.Provider>
  );
}

export default App;