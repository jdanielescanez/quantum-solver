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
import { themeFormat } from '../Redux/reducers/ThemeFunctions/personalizedColorsAndFounts';

export const Welcome = () => {
  const theme = useTheme();
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
              height: '3.5rem',
              [theme.breakpoints.down("lg")]: {
                height: '3rem',
              },
              [theme.breakpoints.down("md")]: {
                height: '3rem',
              },
              [theme.breakpoints.down("sm")]: {
                height: '3rem',
              },
              [theme.breakpoints.down("xs")]: {
                height: '1rem',
              }
            }}
            alt="Quantum Solver Logo"
            src={logo}
          />
          <Typography
            tabIndex={0}
            variant={themeFormat("titleh2")}
            component="h2"
            sx={{
              fontFamily: themeFormat("titleFontFamily"),
              fontWeight: themeFormat("titleFontWeight")
            }}
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
            variant={themeFormat("textSize")}
            component="p"
            sx={{
              fontFamily: themeFormat("textFontFamily"),
              fontWeight: themeFormat("textFontWeight")
            }}
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
            variant={themeFormat("textSize")}
            component="p"
            sx={{
              fontFamily: themeFormat("textFontFamily"),
              fontWeight: themeFormat("textFontWeight")
            }}
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
              backgroundColor: themeFormat("colorButton"),
              borderRadius: 30,
              textAlign: "center"
            }}
          >
            <Typography
              component="span"
              variant={themeFormat("textButton")}
              sx={{
                fontFamily: themeFormat("buttonFontFamily"),
                fontWeight: themeFormat("buttonFontWeight")
              }}
            >
              <RocketIcon sx={{ justifyItems: "center" }}> </RocketIcon> <br></br>
              Start
            </Typography>
          </Button>
        </Box>
      </Container>
    </main>
  );
}