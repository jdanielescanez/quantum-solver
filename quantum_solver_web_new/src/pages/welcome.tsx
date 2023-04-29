// Components
import Banner from '../components/Banner';

// MUI exports
import Container from '@mui/material/Container';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import Button from '@mui/material/Button';
import { useTheme } from '@mui/material';

// Import 
import { Link } from 'react-router-dom';

// Icons
import RocketIcon from '@mui/icons-material/Rocket';

// assets
import LightLogo from '../assets/LightLogo192.png';
import DarkLogo from '../assets/DarkLogo192.png';

// Fuctions
import { colorTokens } from '../Redux/reducers/ThemeFunctions/colorsTokensPallete';


export const Welcome = () => {
  const theme = useTheme();
  const colorButton = colorTokens(theme.palette.mode).blueAccent[500];
  let logo;
  theme.palette.mode === "dark" ? (
    logo = DarkLogo
  ) : (
    logo = LightLogo
  )
  return (
    <main className="WelcomePage">
      <Banner />
      <Container 
        sx={{ 
          marginY: 5, 
          marginBottom: "1em",
          }}>
        <Box
          display="flex"
          justifyContent="center"
          sx={{ flexGrow: 1 }}>
          <Box
            display="flex"
            tabIndex={0}
            aria-label='Quantum Solver Logo'
            component="img"
            marginRight="10px"
            sx={{
              height: '3rem',
              [theme.breakpoints.down("sm")]: {
                height: '2rem',
              }
            }}
            alt="Quantum Solver Logo"
            src={logo}
          />
          <Typography
            tabIndex={0}
            variant='h1'
            component="h2"
            sx={{ fontFamily: '"Helvetica Neue"', fontWeight: "bold" }}
          >
            Quantum Solver
          </Typography>
        </Box>
        <Box
          display="flex"
          justifyContent="center"
          sx={{ flexGrow: 1, marginTop: 2 }}>
          <Typography
            tabIndex={0}
            variant='body1'
            component="p"
            sx={{ fontFamily: '"Helvetica Neue"', fontWeight: "italic" }}
          >
            <b>Open source</b>  quantum library based on <b>Qiskit</b>
          </Typography>
        </Box>
        <Box
          display="flex"
          justifyContent="center"
          sx={{ flexGrow: 1 }}>
          <Typography
            tabIndex={0}
            variant='body1'
            component="p"
            sx={{ fontFamily: '"Helvetica Neue"', fontWeight: "italic" }}
          >
            Use it to simulate <b>quantum algorithms</b> and see their results
          </Typography>
        </Box>
        <Box
          sx={{
            mb: 2,
            marginBottom: "2em",
            marginTop: "2em",
            flexGrow: 1,
            justifyContent: "center",
            display: "flex",
          }}>
          <Button
            tabIndex={0}
            aria-label="Button Start go to login"
            component={Link} to='/login'
            variant="contained"
            size="large"
            sx={{
              backgroundColor: colorButton,
              borderRadius: 30,
              textAlign: "center"
            }}
          >
            <Typography 
              component="span"
              sx={{ 
                fontFamily: '"Helvetica Neue"', 
                fontWeight: "bold" 
              }}>
              <RocketIcon sx={{justifyItems: "center"}}> </RocketIcon> <br></br>
              Start
            </Typography>
          </Button>
        </Box>
      </Container>
    </main>
  );
}