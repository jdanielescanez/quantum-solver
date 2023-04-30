import Box from '@mui/material/Box';
import Grid from '@mui/material/Grid';
import Typography from '@mui/material/Typography';
import Container from '@mui/material/Container';
import { Link as linkMui } from '@mui/material';

// React
import { Link } from 'react-router-dom';

// fuction
import { themeFormat } from '../Redux/reducers/ThemeFunctions/personalizedColorsAndFounts';



export default function Footer() {
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
          color: themeFormat("color"),
          marginTop: "auto",
        }}
      >
        <Container maxWidth="xl" sx={{ display: "flex" }}>
          <Grid container spacing={2} sx={{ marginBottom: "1em", alignContent: "center" }}>
            <Grid item xs={12} sm={4}>
              <Box borderBottom={3} tabIndex={0} aria-label="Link to Web Map">
                <Typography
                  variant={themeFormat("titleh4")}
                  component="h3"
                  sx={{
                    fontFamily: themeFormat("titleFontFamily"),
                    fontWeight: themeFormat("titleFontWeight"),
                  }}
                >
                  <b>Web Map ( 1 ) </b>
                </Typography>
              </Box>
              <Box>
                <Typography
                  tabIndex={0}
                  aria-label="Link to Home page"
                  component={Link} to='/'
                  variant={themeFormat("textSize")}
                  color={themeFormat("colorLinks")}
                  sx={{
                    textDecoration: themeFormat("linksDecoration"),
                    fontFamily: themeFormat("textFontFamily"),
                    fontWeight: themeFormat("linkFontWeight"),
                  }}
                >
                  Home page
                </Typography>
              </Box>
              <Box>
                <Typography
                  tabIndex={0}
                  aria-label="link to login page"
                  component={Link} to='/login'
                  variant={themeFormat("textSize")}
                  color={themeFormat("colorLinks")}
                  sx={{
                    textDecoration: themeFormat("linksDecoration"),
                    fontFamily: themeFormat("textFontFamily"),
                    fontWeight: themeFormat("linkFontWeight"),
                  }}
                >
                  Login Page
                </Typography>
              </Box>
              <Box>
                <Typography
                  tabIndex={0}
                  aria-label="Link to Information Algorithms page"
                  component={Link} to='/algorithms'
                  variant={themeFormat("textSize")}
                  color={themeFormat("colorLinks")}
                  sx={{
                    textDecoration: themeFormat("linksDecoration"),
                    fontFamily: themeFormat("textFontFamily"),
                    fontWeight: themeFormat("linkFontWeight"),
                  }}
                >
                  Algorithms Information
                </Typography>
              </Box>
            </Grid>


            <Grid item xs={12} sm={4}>
              <Box borderBottom={3} tabIndex={0} aria-label="Link to Web Map">
                <Typography
                  variant={themeFormat("titleh4")}
                  component="h3"
                  sx={{
                    fontFamily: themeFormat("titleFontFamily"),
                    fontWeight: themeFormat("titleFontWeight"),
                  }}
                >
                  <b>Web Map ( 2 )</b>
                </Typography>
              </Box>
              <Box>
                <Typography
                  tabIndex={0}
                  aria-label="link to Run Algorithms page"
                  component={Link} to='/algorithmsRun'
                  variant={themeFormat("textSize")}
                  color={themeFormat("colorLinks")}
                  sx={{
                    textDecoration: themeFormat("linksDecoration"),
                    fontFamily: themeFormat("textFontFamily"),
                    fontWeight: themeFormat("linkFontWeight"),
                  }}
                >
                  Run algorithms
                </Typography>
              </Box>
              <Box>
                <Typography
                  tabIndex={0}
                  aria-label="link to accessibility statement page"
                  component={Link} to='/accessibility'
                  variant={themeFormat("textSize")}
                  color={themeFormat("colorLinks")}
                  sx={{
                    textDecoration: themeFormat("linksDecoration"),
                    fontFamily: themeFormat("textFontFamily"),
                    fontWeight: themeFormat("linkFontWeight"),
                  }}
                >
                  Accessibility statement
                </Typography>
              </Box>
              <Box>
                <Typography
                  tabIndex={0}
                  aria-label="link to About us page"
                  component={Link} to='/about'
                  variant={themeFormat("textSize")}
                  color={themeFormat("colorLinks")}
                  sx={{
                    textDecoration: themeFormat("linksDecoration"),
                    fontFamily: themeFormat("textFontFamily"),
                    fontWeight: themeFormat("linkFontWeight"),
                  }}
                >
                  About us
                </Typography>
              </Box>
            </Grid>


            <Grid item xs={12} sm={4}>
              <Box borderBottom={3} tabIndex={0} aria-label="Our Github page">
                <Typography
                  variant={themeFormat("titleh4")}
                  component="h3"
                  sx={{
                    fontFamily: themeFormat("titleFontFamily"),
                    fontWeight: themeFormat("titleFontWeight"),
                  }}
                >
                  <b>Our Github page</b>
                </Typography>
              </Box>
              <Box>
                <Typography
                  tabIndex={0}
                  component={linkMui} href='https://github.com/alu0101238944/quantum-solver' target="_blank"
                  aria-label="link to Github Page"
                  variant={themeFormat("textSize")}
                  color={themeFormat("colorLinks")}
                  sx={{
                    textDecoration: themeFormat("linksDecoration"),
                    fontFamily: themeFormat("textFontFamily"),
                    fontWeight: themeFormat("linkFontWeight"),
                  }}
                >
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