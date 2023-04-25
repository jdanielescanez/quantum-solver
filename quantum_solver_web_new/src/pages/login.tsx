// React -redux imports
import React, { useState } from 'react';
import { useNavigate } from "react-router-dom";
import { useDispatch, useSelector } from 'react-redux';

// MUI imports
import Container from '@mui/material/Container'
import Paper from '@mui/material/Paper'
import Box from '@mui/material/Box'
import Typography from '@mui/material/Typography'
import TextField from '@mui/material/TextField'
import Button from '@mui/material/Button'
import Stack from '@mui/material/Stack'
import Alert from '@mui/material/Alert'
import Accordion from '@mui/material/Accordion';
import AccordionSummary from '@mui/material/AccordionSummary';
import AccordionDetails from '@mui/material/AccordionDetails';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
import { Link as linkMui } from '@mui/material';
import { useTheme } from '@mui/material'

// Fuctions
import { colorTokens } from '../Redux/reducers/ThemeFunctions/colorsTokensPallete';

// components Import 
import { BreadCrumbsComponent } from '../components/breadCrumbs'

// Import Action 
import { login } from '../Redux/actions/LoginActions';

//logo import
import LightLogo from '../assets/LightLogo192.png';
import DarkLogo from '../assets/DarkLogo192.png';

export const Login = () => {
  const theme = useTheme();

  const colorButton = colorTokens(theme.palette.mode).blueAccent[500];
  const colorTarjeta = colorTokens(theme.palette.mode).grey[800];
  const colorTrajetaLight = colorTokens(theme.palette.mode).grey[900];
  const colorLinks = colorTokens(theme.palette.mode).grey[100];

  let logo;
  theme.palette.mode === "dark" ? (
    logo = DarkLogo
  ) : (
    logo = LightLogo
  )

  const dispatch = useDispatch();
  let navigate = useNavigate();

  const [token, setToken] = useState("");
  const [tokenError] = useState("");

  const flagError = useSelector((state: any) => state.login_reducer.flagError);
  const guest = useSelector((state: any) => state.login_reducer.guest);


  const handleTokenLogin = async (e: any) => {
    e.preventDefault();
    await dispatch(login(token, false))
    navigate("/algorithms");
  }

  const routesLogin = ['/login']

  return (
    <div className="login">
      <BreadCrumbsComponent routes={routesLogin} />
      <Container
        maxWidth="xl"
        sx={{
          marginY: 1,
          marginBottom: "2em",
          minHeight: "60vh",
        }}>
        <Paper
          elevation={3}
          sx={{
            padding: 2,
            margin: 2,
            borderRadius: 10,
          }}>
          <Box
            sx={{
              padding: 2,
              justifyContent: "center",
              alignContent: "center",
              display: "flex",
              marginTop: "2em",
              marginBottom: "2em",
            }}>
            <Stack
              spacing={2}
              alignItems="center">
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
              <Box
                sx={{
                  justifyContent: "center",
                  display: "flex",
                }}>
                <Typography
                  tabIndex={0}
                  variant="h2"
                  component="h2"
                  align="center"
                  sx={{ fontFamily: '"Helvetica Neue"', fontWeight: "bold" }}
                >
                  Login Page
                </Typography>
              </Box>
              <Box
                sx={{
                  justifyContent: "center",
                  display: "flex",
                }}>
                <Typography
                  tabIndex={0}
                  variant="body1"
                  component="p"
                  sx={{ fontFamily: '"Helvetica Neue"', fontWeight: "italic" }}>
                  Enter your&nbsp;
                  <Typography
                    tabIndex={0}
                    variant='body1'
                    color={colorLinks}
                    aria-label="IBM token Information link"
                    component={linkMui} href='https://quantum-computing.ibm.com/composer/docs/iqx/manage/account/'
                    sx={{
                      textDecoration: "underline",
                      fontFamily: '"Helvetica Neue"',
                      fontWeight: "italic",
                    }}>
                    IBM Token
                  </Typography>
                  &nbsp;to login
                </Typography>

              </Box>
              <form className="registerForm" onSubmit={handleTokenLogin}>
                <TextField
                  label="Enter your token here"
                  type={'text'}
                  value={token}
                  required={true}
                  aria-required="true"
                  variant="outlined"
                  color={theme.palette.mode === "dark" ? "secondary" : "primary"}
                  margin="dense"
                  placeholder="your token"
                  onChange={(e) => setToken(e.target.value)}
                  error={tokenError !== ""}
                  helperText={tokenError}
                  sx={{
                    width: "100%"
                  }}
                />
                {flagError === "none" && guest === false &&
                  <Alert
                    sx={{
                      fontFamily: '"Helvetica Neue"',
                      fontWeight: "bold",
                    }}
                    severity="success"
                    variant="filled">
                    {"Valid Token 😄"}
                  </Alert>
                }
                {flagError === "error" &&
                  <Alert
                    sx={{
                      fontFamily: '"Helvetica Neue"',
                      fontWeight: "bold",
                    }}
                    severity="error"
                    variant="filled">
                    {"Invalid Token. Try Again 😞"}
                  </Alert>
                }
                <Box
                  sx={{
                    justifyContent: "center",
                    display: "flex",
                  }}>
                  <Button
                    tabIndex={0}
                    aria-label='Login Button with token and go to the algorithm page'
                    type="submit"
                    variant="contained"
                    sx={{
                      borderRadius: 3,
                      backgroundColor: colorButton,
                      justifyContent: "center",
                      marginTop: 2,
                    }}
                  >
                    <Typography sx={{ fontFamily: '"Helvetica Neue"', fontWeight: "bold" }}>
                      let's go
                    </Typography>
                  </Button>
                </Box>
              </form>
              <Box
                sx={{
                  justifyContent: "center",
                }}>
                <Typography
                  tabIndex={0}
                  variant="body1"
                  component="p"
                  sx={{ fontFamily: '"Helvetica Neue"', fontWeight: "italic" }}>
                  or continue as has guest
                </Typography>
              </Box>
              <Box
                sx={{
                  justifyContent: "center",
                  display: "flex",
                }}>
                <Button
                  tabIndex={0}
                  aria-label='Login Button like a Gest and go to the algorithm page'
                  variant="contained"
                  sx={{
                    borderRadius: 3,
                    backgroundColor: colorButton,
                    justifyContent: "center",
                  }}
                  onClick={() => {
                    dispatch(login("", true))
                    navigate("/algorithms");
                  }}
                >
                  <Typography
                    variant='body1'
                    component='p'
                    sx={{
                      fontFamily: '"Helvetica Neue"',
                      fontWeight: "bold"
                    }}>
                    continue as guest
                  </Typography>
                </Button>
              </Box>
              {flagError === "none" && guest === true &&
                <Alert
                  sx={{
                    fontFamily: '"Helvetica Neue"',
                    fontWeight: "bold",
                  }}
                  severity="success"
                  variant="filled">
                  {"Valid Guest mode Login 😄"}
                </Alert>
              }
            </Stack>
          </Box>
          <Box
            sx={{
              padding: "2%",
            }}
          >
            <Accordion
              sx={{
                borderRadius: 2,
                padding: "2%",
                bgcolor: theme.palette.mode === 'dark' ? colorTarjeta : colorTrajetaLight,
              }}>
              <AccordionSummary
                expandIcon={<ExpandMoreIcon />}
                aria-controls="panel1a-content"
                id="panel1a-header"
              >
                <Typography
                  tabIndex={0}
                  variant="body1"
                  component="p"
                  justifyContent="left"
                  sx={{
                    fontFamily: '"Helvetica Neue"',
                    fontWeight: "italic",
                    marginLeft: "1em"
                  }}>
                  More information about the IBM Token
                </Typography>
              </AccordionSummary>
              <AccordionDetails>
                <Box
                  sx={{
                    display: "flex",
                    flexDirection: "column",
                    marginTop: "1em",
                    marginBottom: "1em",
                  }}>
                  <Typography
                    tabIndex={0}
                    variant="body1"
                    component="p"
                    justifyContent="left"
                    sx={{
                      fontFamily: '"Helvetica Neue"',
                      fontWeight: "italic",
                      marginLeft: "1em"
                    }}>
                    The toolset uses your personal IBM Quantum Experience token to access to the IBM hardware.
                    You can access to your API token or generate another one&nbsp;
                    <Typography
                      tabIndex={0}
                      variant='body1'
                      color={colorLinks}
                      aria-label="IBM login page link"
                      component={linkMui} href='https://quantum-computing.ibm.com/account'
                      sx={{
                        textDecoration: "underline",
                        fontFamily: '"Helvetica Neue"',
                        fontWeight: "italic",
                      }}>
                      here (IBM login page)
                    </Typography>
                  </Typography>
                </Box>
                <Box
                  sx={{
                    justifyContent: "left",
                    display: "flex",
                    flexDirection: "column",
                    marginTop: "1em",
                    marginBottom: "1em",
                  }}>
                  <Typography
                    tabIndex={0}
                    variant="body1"
                    component="p"
                    justifyContent="left"
                    sx={{
                      fontFamily: '"Helvetica Neue"',
                      fontWeight: "italic",
                      marginLeft: "1em"
                    }}>
                    You can also use the Guest Mode which only allows you to run quantum circuits in a local simulator ("aer_simulator").
                  </Typography>
                </Box>
              </AccordionDetails>
            </Accordion>
          </Box>
        </Paper>
      </Container>
    </div>
  );
}
