// MUI imports
import Typography from '@mui/material/Typography';
import Breadcrumbs from '@mui/material/Breadcrumbs';
import Box from '@mui/material/Box';
import Paper from '@mui/material/Paper';
import { useTheme } from '@mui/material';


// react-router-dom imports
import { Link } from 'react-router-dom';

// function imports
import { colorTokens } from '../Redux/reducers/ThemeFunctions/colorsTokensPallete';

export const BreadCrumbsComponent = (routes: any) => {
  const theme = useTheme();
  const color = colorTokens(theme.palette.mode).primary[100];
  const colorLinks = colorTokens(theme.palette.mode).grey[100];

  const nameMap: {
    [key: string]: string;
    '/accessibility': string;
    '/login': string;
    '/algorithms': string;
    '/algorithmsRun': string;
    '/about': string;
  } = {
    '/accessibility': 'Accessibility statement',
    '/login': 'Login',
    '/algorithms': 'Algorithms information',
    '/algorithmsRun': 'Run algorithms ',
    '/about': 'About us',
  };
  return (
    <div role="presentation">
      <Box
        sx={{
          display: 'flex',
          justifyContent: 'center',
          alignItems: 'center',
          width: '100%',
        }}
      >
        <Paper
          elevation={3}
          sx={{
            padding: 4,
            margin: "auto",
            borderRadius: 4,
          }}
        >
          <Breadcrumbs tabIndex={0} separator="›" aria-label="breadcrumb">
            <Typography
              tabIndex={0}
              variant='body1'
              color={colorLinks}
              aria-label="link to home page"
              component={Link} to='/'
              sx={{
                fontFamily: '"Helvetica Neue"',
                fontWeight: "italic"
              }}>
              Home
            </Typography>
            {
              routes.routes.map((route: string, i:number) => (
                <Typography
                  key={"breadcrumbs" + i}
                  tabIndex={0}
                  variant='body1'
                  color={colorLinks}
                  aria-label={"link to " + nameMap[route] + " page"}
                  component={Link} to={route}
                  sx={{
                    fontFamily: '"Helvetica Neue"',
                    fontWeight: "italic"
                  }}>
                  {nameMap[route]}
                </Typography>
              ))
            }
          </Breadcrumbs>
        </Paper>
      </Box>
    </div>
  );
}