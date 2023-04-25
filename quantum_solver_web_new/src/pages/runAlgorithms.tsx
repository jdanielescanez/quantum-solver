//import React-Redux
import React from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { useNavigate } from 'react-router-dom'

// MUI imports
import Container from '@mui/material/Container'
import Paper from '@mui/material/Paper'
import Box from '@mui/material/Box'
import Typography from '@mui/material/Typography'
import Alert from '@mui/material/Alert'
import Button from '@mui/material/Button'
import Stack from '@mui/material/Stack'
import TextField from '@mui/material/TextField'
import { useTheme } from '@mui/material'

//Fuctions
import { colorTokens } from '../Redux/reducers/ThemeFunctions/colorsTokensPallete';

//import actions
import {
  getBackendAlgorithmsParams,
  getBackendData,
  getAlgorithmData,
  getParamsData,
} from '../Redux/actions/getBackendAlgorithmParams'

import {
  runNormalMode,
  runExperimentalMode,
  setNShots
} from '../Redux/actions/runActions';

// components Import 
import RunAlgorithmsForm1 from '../components/runAlgorithmsForm1'
import RunAlgorithmsForm2 from '../components/runAlgorithmsForm2'
import { RunAlgorithmsResult } from '../components/runAlgorithmResult'
import { BreadCrumbsComponent } from '../components/breadCrumbs'

const getAllData = async (dispatch: any, token: string) => {
  await dispatch(getBackendAlgorithmsParams(token))
  await dispatch(getBackendData(token))
  await dispatch(getAlgorithmData(token))
}

const getParamsDataFunction = async (dispatch: any, token: string) => {
  await dispatch(getParamsData(token))
}

const runNormalModeFunction = async (dispatch: any, token: string) => {
  await dispatch(runNormalMode(token))
}

const runExperimentalModeFunction = async (dispatch: any, token: string, nShots: number) => {
  await dispatch(runExperimentalMode(token, nShots))
}

export const RunAlgorithms = () => {
  const dispatch = useDispatch();
  const theme = useTheme();
  const colorButton = colorTokens(theme.palette.mode).blueAccent[500];
  const navigate = useNavigate()
  const { token } = useSelector((state: any) => state.login_reducer)
  const { isToken } = useSelector((state: any) => state.login_reducer)

  const allBackends = useSelector((state: any) => state.runAlgorithms_reducer.backendData);
  const allAlgorithms = useSelector((state: any) => state.runAlgorithms_reducer.algorithmsData);
  const allParams = useSelector((state: any) => state.runAlgorithms_reducer.paramsData);

  const currentBackend = useSelector((state: any) => state.runAlgorithms_reducer.currentBackend);
  const currentAlgorithm = useSelector((state: any) => state.runAlgorithms_reducer.currentAlgorithm);
  const paramsData = useSelector((state: any) => state.runAlgorithms_reducer.paramsData.params);

  const [nShots, setnShots] = React.useState('');
  const n_shots = useSelector((state: any) => state.runAlgorithms_reducer.n_shots);

  console.log("n_shots", n_shots)

  const runMode = useSelector((state: any) => state.runAlgorithms_reducer.RunMode);
  const algorithmRun = useSelector((state: any) => state.runAlgorithms_reducer.RunAlgorithmData);

  const handleShots = (event: any) => {
    setnShots(event.target.value);
  };

  const setNShotsFunction = async (e: any) => {
    e.preventDefault();
    dispatch(setNShots(Number(nShots)))
  }

  if (isToken && allBackends === "" && allAlgorithms === "") {
    getAllData(dispatch, token)
  }

  if (isToken && currentBackend !== "" && currentAlgorithm !== "" && allParams === "None") {
    getParamsDataFunction(dispatch, token)
  }

  if (isToken && runMode === 'normal' && algorithmRun === "") {
    runNormalModeFunction(dispatch, token)
  }

  if (isToken && runMode === 'experimental' && n_shots !=="" && algorithmRun === "") {
    runExperimentalModeFunction(dispatch, token, Number(n_shots))
  }

  const routesAlgorithmInfo = ['/algorithmsRun']

  return (
    <div className="runAlgorithms">
      <BreadCrumbsComponent routes={routesAlgorithmInfo} />
      <Container
        maxWidth="xl"
        sx={{
          marginY: 1,
          marginBottom: "2em",
          minHeight: "60vh",
        }}
      >
        <Paper
          elevation={3}
          sx={{
            padding: 1,
            margin: 2,
            borderRadius: 10,
          }}
        >
          <Box
            sx={{
              justifyContent: "center",
              alignContent: "center",
              width: "100%",
              display: "flex",
              marginTop: "2em",
              marginBottom: "2em",
            }}
          >
            <Stack spacing={2}
              sx={{
                justifyContent: "center",
                alignContent: "center",
                width: "100%"
              }}>
              <Box
                sx={{
                  justifyContent: "center",
                  alignContent: "center",
                  display: "flex",
                }}>
                <Typography
                  tabIndex={0}
                  variant="h2"
                  component="h2"
                  sx={{
                    fontFamily: '"Helvetica Neue"',
                    fontWeight: "bold",
                  }}
                >
                  Run Algorithms
                </Typography>
              </Box>
              {
                token === "" ?
                  <>
                    <Box
                      sx={{
                        justifyContent: "center",
                        alignContent: "center",
                        display: "flex",
                      }}>
                      <Button
                        tabIndex={0}
                        aria-label='Go to Login Page'
                        variant="contained"
                        onClick={() => navigate('/login')}
                        sx={{
                          borderRadius: 3,
                          backgroundColor: colorButton,
                          justifyContent: "center",
                          marginTop: 2,
                        }}
                      >
                        <Typography
                          component="span"
                          sx={{
                            fontFamily: '"Helvetica Neue"',
                            fontWeight: "bold",
                          }}>
                          Go to Login Page
                        </Typography>
                      </Button>
                    </Box>
                    <Box
                      sx={{
                        justifyContent: "center",
                        alignContent: "center",
                        display: "flex",
                      }}>
                      <Alert severity="warning"
                        variant="filled"
                        sx={{
                          fontFamily: '"Helvetica Neue"',
                          fontWeight: "bold",
                          color: "black",
                        }}
                      >
                        {"You need to be logged in to run algorithms "}</Alert>
                    </Box>
                  </>
                  :
                  null
              }
              {
                isToken
                  && allBackends === "" && allAlgorithms === "" && allParams === "" ?
                  <>
                    <Typography
                      variant='h3'
                      component="p"
                      sx={{
                        fontFamily: '"Helvetica Neue"',
                        fontWeight: "bold"
                      }}>
                      Loading...
                    </Typography>
                  </>
                  :
                  null
              }
              {
                isToken
                  && allBackends !== "None" && allAlgorithms !== "None" && allParams === "None"
                  && currentBackend === "" && currentAlgorithm === "" ?
                  < RunAlgorithmsForm1 allBackends={allBackends} allAlgorithms={allAlgorithms} />
                  :
                  null
              }
              {
                isToken
                  && currentBackend !== "" && currentAlgorithm !== "" && paramsData ?
                  < RunAlgorithmsForm2 params={paramsData} />
                  :
                  null
              }
              {isToken && runMode === 'normal' && algorithmRun === "" ?
                <Box sx={{
                  justifyContent: "center",
                  alignContent: "center",
                  display: "flex",
                  marginTop: "2em",
                  marginBottom: "2em"
                }}>
                  <Typography
                    tabIndex={0}
                    variant='h3'
                    component="p"
                    sx={{
                      fontFamily: '"Helvetica Neue"',
                      fontWeight: "bold"
                    }}>
                    Running Algorithm...
                  </Typography>
                </Box>
                :
                null
              }
              {
                isToken
                  && runMode === 'normal' && algorithmRun !== "" ?
                  < RunAlgorithmsResult />
                  :
                  null
              }
              {
                isToken
                  && runMode === 'experimental' && n_shots === "" && algorithmRun === "" ?
                  <Box
                    sx={{
                      justifyContent: "center",
                      alignContent: "center",
                      display: "flex",
                      marginTop: "2em",
                      marginBottom: "2em",
                    }}>
                    <form className="nshotsForm" onSubmit={setNShotsFunction}>
                      <div>
                        <Typography
                          tabIndex={0}
                          variant="body1"
                          component="p"
                          sx={{
                            fontFamily: '"Helvetica Neue"',
                            fontWeight: "italic",
                            marginTop: 1,
                            marginBottom: 3,
                          }}>
                          Insert n_shots :
                        </Typography>
                        <TextField
                          aria-label={"insert n_shots"}
                          aria-required="true"
                          id="n_shots"
                          type="number"
                          required
                          label={"insert n_shots"}
                          onChange={handleShots}
                          color={theme.palette.mode === "dark" ? "secondary" : "primary"}
                          sx={{
                            width: "100%",
                          }}
                        />
                      </div>

                      <Button
                        tabIndex={0}
                        aria-label='Set backend and algorithm'
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
                          Set backend and algorithm
                        </Typography>
                      </Button>
                    </form>
                  </Box>
                  :
                  null
              }
              {
                isToken
                  && runMode === 'experimental' && n_shots !== "" && algorithmRun === "" ?
                  <Box
                    sx={{
                      justifyContent: "center",
                      alignContent: "center",
                      display: "flex",
                      marginTop: "2em",
                      marginBottom: "2em",
                    }}>
                    <Typography
                      tabIndex={0}
                      variant='h3'
                      component="p"
                      sx={{
                        fontFamily: '"Helvetica Neue"',
                        fontWeight: "bold",
                      }}
                    >
                      Running Algorithm in Experimental mode...
                    </Typography>
                  </Box>
                  :
                  null
              }
              {
                isToken
                  && runMode === 'experimental' && algorithmRun !== "" ?
                  < RunAlgorithmsResult />
                  :
                  null
              }
            </Stack>
          </Box>
        </Paper>
      </Container >
    </div >
  );
}
