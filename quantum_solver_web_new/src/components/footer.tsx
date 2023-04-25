import Box from '@mui/material/Box';
import Grid from '@mui/material/Grid';
import Typography from '@mui/material/Typography';
import Container from '@mui/material/Container';
import { Link as linkMui } from '@mui/material';
import { useTheme } from '@mui/material';

// React
import { Link } from 'react-router-dom';
// fuction
import { colorTokens } from '../Redux/reducers/ThemeFunctions/colorsTokensPallete';

export default function Footer() {
  const theme = useTheme();
  const color = colorTokens(theme.palette.mode).primary[100];
  const colorLinks = colorTokens(theme.palette.mode).grey[100];

  return (
    <footer className='Footer'>
      <Box
        tabIndex={0}
        aria-label="Footer of the page"
        sx={{
          position: "static",
          bottom: 0,
          height: "100%",
          justifyContent: "center",
          alignItems: "center",
          color: { color },
          marginTop: "auto",
        }}
      >
        <Container maxWidth="xl" sx={{ display: "flex" }}>
          <Grid container spacing={2} sx={{ marginBottom: "1em", alignContent: "center" }}>

            <Grid item xs={14} sm={3}>
              <Box borderBottom={3} tabIndex={0} aria-label="Authors" >
                <Typography  
                  variant='body1' 
                  component="h3"
                  sx={{
                    fontFamily: '"Helvetica Neue"', 
                    fontWeight: "bold"
                  }}
                  >
                  <b>Authors</b>
                </Typography>
              </Box>
              <Box>
                <Typography 
                  tabIndex={0} 
                  variant='body1'
                  component="p"
                  sx={{
                    fontFamily: '"Helvetica Neue"', 
                    fontWeight: "italic"
                  }}
                  >
                  Daniel Escánez-Expósito
                </Typography>
              </Box>
              <Box>
                <Typography 
                  tabIndex={0} 
                  variant='body1'
                  component="p"
                  sx={{
                    fontFamily: '"Helvetica Neue"', 
                    fontWeight: "italic"
                  }}
                  >
                  Vlatko Marchán-Sekulic
                </Typography>
              </Box>
              <Box>
                <Typography 
                  tabIndex={0} 
                  variant='body1'
                  component="p"
                  sx={{
                    fontFamily: '"Helvetica Neue"', 
                    fontWeight: "italic"
                  }}
                  >
                  Andrea Hernández-Martín
                </Typography>
              </Box>
            </Grid>


            <Grid item xs={14} sm={3}>
              <Box borderBottom={3} tabIndex={0} aria-label="Link to Web Map">
                <Typography 
                  variant='body1'
                  component="h3"
                  sx={{
                    fontFamily: '"Helvetica Neue"', 
                    fontWeight: "bold"
                  }}>
                  <b>Web Map ( 1 ) </b>
                </Typography>
              </Box>
              <Box>
                <Typography
                  tabIndex={0}
                  variant='body1'
                  color={colorLinks}
                  aria-label="Link to Home page"
                  component={Link} to='/'
                  sx={{
                    fontFamily: '"Helvetica Neue"', 
                    fontWeight: "italic"
                  }}
                  >
                  Home page
                </Typography>
              </Box>
              <Box>
                <Typography
                  tabIndex={0}
                  variant='body1'
                  color={colorLinks}
                  aria-label="link to login page"
                  component={Link} to='/login'
                  sx={{
                    fontFamily: '"Helvetica Neue"', 
                    fontWeight: "italic"
                  }}
                  >
                  Login Page
                </Typography>
              </Box>
              <Box>
                <Typography
                  tabIndex={0}
                  variant='body1'
                  color={colorLinks}
                  aria-label="Link to Information Algorithms page"
                  component={Link} to='/algorithms'
                  sx={{
                    fontFamily: '"Helvetica Neue"', 
                    fontWeight: "italic"
                  }}
                  >
                  Algorithms Information
                </Typography>
              </Box>
            </Grid>


            <Grid item xs={14} sm={3}>
              <Box borderBottom={3} tabIndex={0} aria-label="Link to Web Map">
                <Typography 
                  variant='body1'
                  component="h3"
                  sx={{
                    fontFamily: '"Helvetica Neue"', 
                    fontWeight: "bold"
                  }}>
                  <b>Web Map ( 2 )</b>
                </Typography>
              </Box>
              <Box>
                <Typography
                  tabIndex={0}
                  variant='body1'
                  color={colorLinks}
                  aria-label="link to Run Algorithms page"
                  component={Link} to='/algorithmsRun'
                  sx={{
                    fontFamily: '"Helvetica Neue"', 
                    fontWeight: "italic"
                  }}>
                  Run algorithms
                </Typography>
              </Box>
              <Box>
                <Typography
                  tabIndex={0}
                  variant='body1'
                  color={colorLinks}
                  aria-label="link to accessibility statement page"
                  component={Link} to='/accessibility'
                  sx={{
                    fontFamily: '"Helvetica Neue"', 
                    fontWeight: "italic"
                  }}>
                  Accessibility statement
                </Typography>
              </Box>
              <Box>
                <Typography
                  tabIndex={0}
                  variant='body1'
                  color={colorLinks}
                  aria-label="link to About us page"
                  component={Link} to='/about'
                  sx={{
                    fontFamily: '"Helvetica Neue"', 
                    fontWeight: "italic"
                  }}>
                  About us
                </Typography>
              </Box>
            </Grid>


            <Grid item xs={14} sm={3}>
              <Box borderBottom={3} tabIndex={0} aria-label="Our Github page">
                <Typography 
                variant='body1'
                component="h3"
                sx={{
                  fontFamily: '"Helvetica Neue"', 
                  fontWeight: "bold"
                }}>
                  <b>Our Github page</b>
                </Typography>
              </Box>
              <Box>
                <Typography
                  tabIndex={0}
                  variant='body1'
                  color={colorLinks}
                  aria-label="link to Github Page"
                  component={linkMui} href='https://github.com/alu0101238944/quantum-solver'
                  sx={{
                    textDecoration: "underline", 
                    fontFamily: '"Helvetica Neue"', 
                    fontWeight: "italic"
                  }}>
                  Github repository
                </Typography>
              </Box>
            </Grid>
          </Grid>
        </Container>
      </Box>
    </footer>
  );
}