//import React-Redux
import React from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { useNavigate } from 'react-router-dom'
import { Link } from 'react-router-dom';

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

//icons 
import CircularProgress from '@mui/material/CircularProgress';

//Fuctions
import { themeFormat } from '../Redux/reducers/ThemeFunctions/personalizedColorsAndFounts';

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
  setNShots,
  clearExecutionData
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
  const navigate = useNavigate()
  const theme = useTheme();

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

  const runMode = useSelector((state: any) => state.runAlgorithms_reducer.RunMode);
  const algorithmRun = useSelector((state: any) => state.runAlgorithms_reducer.RunAlgorithmData);

  const handleShots = (event: any) => {
    setnShots(event.target.value);
  };

  const setNShotsFunction = async (e: any) => {
    e.preventDefault();
    dispatch(setNShots(Number(nShots)))
  }

  const clearExecutionDataFunction = (e: any) => {
    e.preventDefault();
    dispatch(clearExecutionData());
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

  if (isToken && runMode === 'experimental' && n_shots !== "" && algorithmRun === "") {
    runExperimentalModeFunction(dispatch, token, Number(n_shots))
  }

  const routesAlgorithmInfo = ['/login', '/algorithmsRun']

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
            minHeight: "60vh",
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
                  variant={themeFormat("titleh2")}
                  component="h2"
                  sx={{
                    fontFamily: themeFormat("titleFontFamily"),
                    fontWeight: themeFormat("titleFontWeight")
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
                          backgroundColor: themeFormat("colorButton"),
                          justifyContent: "center",
                          marginTop: 2,
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
                        variant={themeFormat("alertVariant")}
                        sx={{
                          fontFamily: themeFormat("alertsFontFamily"),
                          fontWeight: themeFormat("alertsFontWeight"),
                          color: themeFormat("warning"),
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
                    <Box
                      sx={{
                        justifyContent: "center",
                        alignContent: "center",
                        display: "flex",
                        marginTop: "2em",
                        marginBottom: "2em",
                      }}>
                      <CircularProgress
                        tabIndex={0}
                        aria-label='loading data'
                        color={theme.palette.mode === "dark" ? "secondary" : "primary"}
                      />
                      <Typography
                        tabIndex={0}
                        variant={themeFormat("titleh3")}
                        component="p"
                        sx={{
                          fontFamily: themeFormat("titleFontFamily"),
                          fontWeight: themeFormat("titleFontWeight")
                        }}
                      >
                        &nbsp;Loading...
                      </Typography>
                    </Box>
                  </>
                  :
                  null
              }
              {
                isToken
                  && allBackends !== "None" && allAlgorithms !== "None" && allParams === "None"
                  && currentBackend === "" && currentAlgorithm === "" ?
                  <>
                    < RunAlgorithmsForm1 allBackends={allBackends} allAlgorithms={allAlgorithms} />
                    <Box
                      sx={{
                        padding: 2,
                        justifyContent: "center",
                        display: "flex",
                      }}>
                      <Typography
                        tabIndex={0}
                        variant={themeFormat("textSize")}
                        component="p"
                        sx={{
                          fontFamily: themeFormat("textFontFamily"),
                          fontWeight: themeFormat("textFontWeight")
                        }}
                      >
                        You can see all the information on how the algorithms works on&nbsp;
                        <Typography
                          tabIndex={0}
                          aria-label="link to Run Algorithms page"
                          component={Link} to='/algorithms'
                          variant={themeFormat("textSize")}
                          color={themeFormat("colorLinks")}
                          sx={{
                            textDecoration: themeFormat("linksDecoration"),
                            fontFamily: themeFormat("textFontFamily"),
                            fontWeight: themeFormat("linkFontWeight"),
                          }}
                        >
                          Algorithm Information.
                        </Typography>
                      </Typography>
                    </Box>
                  </>
                  :
                  null
              }
              {
                isToken
                  && currentBackend !== "" && currentAlgorithm !== "" && paramsData ?
                  <>
                    < RunAlgorithmsForm2 params={paramsData} />
                  </>
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
                  <CircularProgress
                    color={theme.palette.mode === "dark" ? "secondary" : "primary"}
                  />
                  <Typography
                    tabIndex={0}
                    variant={themeFormat("titleh3")}
                    component="p"
                    sx={{
                      fontFamily: themeFormat("titleFontFamily"),
                      fontWeight: themeFormat("titleFontWeight")
                    }}
                  >
                    &nbsp;Running Algorithm...
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
                  <>
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
                            variant={themeFormat("titleh4")}
                            component="p"
                            sx={{
                              fontFamily: themeFormat("titleFontFamily"),
                              fontWeight: themeFormat("titleFontWeight"),
                              marginBottom: "1em"
                            }}
                          >
                            Insert n_shots
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
                              marginBottom: "1em",
                              fontFamily: themeFormat("textFontFamily")
                            }}
                          />
                        </div>

                        <Box
                          sx={{
                            justifyContent: "center",
                            alignContent: "center",
                            display: "flex",
                          }}>
                          <Button
                            tabIndex={0}
                            aria-label='Set n_shots'
                            type="submit"
                            variant="contained"
                            sx={{
                              borderRadius: 3,
                              backgroundColor: themeFormat("colorButton"),
                              justifyContent: "center",
                              marginTop: 2,
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
                              Set n_shots
                            </Typography>
                          </Button>
                        </Box>
                      </form>
                    </Box>
                    <Stack>
                      <Box
                        sx={{
                          width: "100%",
                          justifyContent: "center",
                          alignContent: "center",
                          display: "flex"
                        }}
                      >
                        <Typography
                          tabIndex={0}
                          variant={themeFormat("textSize")}
                          component="p"
                          sx={{
                            fontFamily: themeFormat("textFontFamily"),
                            fontWeight: themeFormat("textFontWeight"),
                            marginTop: 2,
                            marginBottom: 1,
                          }}
                        >
                          OR
                        </Typography>
                      </Box>
                      <Box
                        sx={{
                          justifyContent: "center",
                          alignContent: "center",
                          display: "flex"
                        }}
                      >
                        <Button
                          tabIndex={0}
                          aria-label='Go back'
                          onClick={clearExecutionDataFunction}
                          variant="contained"
                          sx={{
                            borderRadius: 3,
                            backgroundColor: themeFormat("colorButton"),
                            justifyContent: "center",
                            marginTop: 2,
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
                            Go back
                          </Typography>
                        </Button>
                      </Box>
                    </Stack>
                  </>
                  :
                  null
              }
              {
                isToken
                  && runMode === 'experimental' && n_shots !== "" && algorithmRun === "" ?
                  <Box
                    tabIndex={0}
                    aria-label='loading gif'
                    sx={{
                      justifyContent: "center",
                      alignContent: "center",
                      display: "flex",
                      marginTop: "2em",
                      marginBottom: "2em",
                    }}>
                    <CircularProgress
                      color={theme.palette.mode === "dark" ? "secondary" : "primary"}
                    />
                    <Typography
                      tabIndex={0}
                      variant={themeFormat("titleh3")}
                      component="p"
                      sx={{
                        fontFamily: themeFormat("titleFontFamily"),
                        fontWeight: themeFormat("titleFontWeight")
                      }}
                    >
                      &nbsp;Running Algorithm in Experimental mode...
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
