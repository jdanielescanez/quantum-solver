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
import { useTheme } from '@mui/material'

// Fuctions
import { colorTokens } from '../Redux/reducers/ThemeFunctions/colorsTokensPallete';

// Import Action 
import { login } from '../Redux/actions/LoginActions';

//logo import
import LightLogo from '../assets/LightLogo192.png';
import DarkLogo from '../assets/DarkLogo192.png';

export const Login = () => {
  const theme = useTheme();
  const colorButton = colorTokens(theme.palette.mode).blueAccent[500];
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

  return (
    <div className="login">
      <Container
        maxWidth="xl"
        sx={{
          marginY: 5,
          marginBottom: "2em",
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
                  component="h1"
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
                  Enter your IBM Token to login
                </Typography>
              </Box>
              <form className="registerForm" onSubmit={handleTokenLogin}>
                <TextField
                  label="Enter your token here"
                  type={'text'}
                  value={token}
                  required={true}
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
                  <Alert sx={{ marginTop: 2 }} severity="success" variant="filled">{"Valid Token 😄"}</Alert>
                }
                {flagError === "error" &&
                  <Alert sx={{ marginTop: 2 }} severity="error" variant="filled">{"Invalid Token. Try Again 😞"}</Alert>
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
                  <Typography sx={{ fontFamily: '"Helvetica Neue"', fontWeight: "bold" }}>
                    continue as guest
                  </Typography>
                </Button>
              </Box>
              {flagError === "none" && guest === true &&
                <Alert sx={{ marginTop: 2 }} severity="success" variant="filled">{"Valid Guest mode Login 😄"}</Alert>
              }
            </Stack>
          </Box>
        </Paper>
      </Container>
    </div>
  );
}
