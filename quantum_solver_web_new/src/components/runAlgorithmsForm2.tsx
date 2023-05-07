//redux-react 
import { useDispatch, useSelector } from 'react-redux';

//MUI imports
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import TextField from '@mui/material/TextField';
import Stack from '@mui/material/Stack';
import Button from '@mui/material/Button';
import Grid from '@mui/material/Grid';
import Alert from '@mui/material/Alert';
import Accordion from '@mui/material/Accordion';
import AccordionSummary from '@mui/material/AccordionSummary';
import AccordionDetails from '@mui/material/AccordionDetails';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
import { useTheme } from '@mui/material';

//Fuctions
import { themeFormat } from '../Redux/reducers/ThemeFunctions/personalizedColorsAndFounts';

// import actions
import {
  clearBackendAlgorithmsParams
} from '../Redux/actions/getBackendAlgorithmParams';
import {
  setCurrentParams
} from '../Redux/actions/setBackendAlgorithmParams';
import {
  setRunMode,
} from '../Redux/actions/runActions';

type Param = {
  'type': string,
  'description': string,
  'constraint': string
};


const RunAlgorithmsForm2 = ({ params }: any) => {

  const { token } = useSelector((state: any) => state.login_reducer)
  const err = useSelector((state: any) => state.runAlgorithms_reducer.currentParams.err);
  const msg = useSelector((state: any) => state.runAlgorithms_reducer.currentParams.msg);
  const runMode = useSelector((state: any) => state.runAlgorithms_reducer.RunMode);

  const dispatch = useDispatch();

  const theme = useTheme();

  const params_value: any = [''];


  const clearData = (e: any) => {
    e.preventDefault();
    dispatch(clearBackendAlgorithmsParams());
  }

  const runNormal = (e: any) => {
    e.preventDefault();
    dispatch(setRunMode('normal'));
  }

  const runExperimental = (e: any) => {
    e.preventDefault();
    dispatch(setRunMode('experimental'));
  }

  const changeParams = (e: any) => {
    params_value[parseInt(e.target.id)] = e.target.value;
  }

  const setParams = (e: any) => {
    e.preventDefault();
    dispatch(setCurrentParams(token, params_value));
  }

  return (
    <Box
      sx={{
        width: "100%",
        margin: "0 auto",
        padding: "0 10%",
      }}
    >
      {
        runMode === "None" ?
          <>
            <Box
              sx={{
                justifyContent: "center",
                alignContent: "center",
                display: "flex",
              }}>
              <Typography
                tabIndex={0}
                variant={themeFormat("titleh3",theme)}
                component="p"
                sx={{
                  fontFamily: themeFormat("titleFontFamily",theme),
                  fontWeight: themeFormat("textFontWeight",theme),
                  textAlign: "left",
                }}

              >
                Set Parameters
              </Typography>
            </Box>
            <Box sx={{
              width: "100%",
              justifyContent: "center",
              alignContent: "center",
              display: "flex"
            }}>
              <Stack spacing={2}>
                <form className="paramsForm" onSubmit={setParams}>
                  {
                    params.map((item: Param, i: number) => {
                      let type: string = '';
                      switch (item.type) {
                        case 'int':
                        case 'float':
                          type = 'number';
                          break;

                        default:
                          type = 'text';
                          break;
                      }
                      return (
                        <div key={i}>
                          <Typography
                            tabIndex={0}
                            variant={themeFormat("textSize",theme)}
                            component="p"
                            sx={{
                              fontFamily: themeFormat("textFontFamily",theme),
                              fontWeight: themeFormat("textFontWeight",theme),
                              marginTop: 1,
                              marginBottom: 3,
                            }}>
                            Insert param {i + 1}:
                          </Typography>
                          <TextField
                            aria-label={item.description}
                            id={i.toString()}
                            aria-required="true"
                            type={type}
                            required
                            label={item.description}
                            onChange={changeParams}
                            color={theme.palette.mode === "dark" ? "secondary" : "primary"}
                            helperText={item.constraint}
                            sx={{
                              width: "100%",
                              fontFamily: themeFormat("textFontFamily",theme),
                              fontWeight: themeFormat("textFontWeight",theme)
                            }}
                          />
                        </div>
                      );
                    })
                  }

                  {
                    err && msg !== "" && runMode === "None" ?
                      <Box
                        sx={{
                          justifyContent: "center",
                          alignContent: "center",
                          display: "flex",
                          marginTop: 2,
                          marginBottom: 2,
                        }}>
                        <Alert severity="error"
                          variant={themeFormat("alertVariant",theme)}
                          sx={{
                            fontFamily: themeFormat("alertsFontFamily",theme),
                            fontWeight: themeFormat("alertsFontWeight",theme),
                            color: themeFormat("error",theme),
                          }}
                        >
                          {msg}
                        </Alert>
                      </Box>
                      :
                      null
                  }
                  {
                    err == false && msg !== "" && runMode === "None" ?
                      <Box
                        sx={{
                          justifyContent: "center",
                          alignContent: "center",
                          display: "flex",
                          marginTop: 2,
                          marginBottom: 2,
                        }}>
                        <Alert severity="success"
                          variant={themeFormat("alertVariant",theme)}
                          sx={{
                            fontFamily: themeFormat("alertsFontFamily",theme),
                            fontWeight: themeFormat("alertsFontWeight",theme),
                            color: themeFormat("success",theme),
                          }}
                        >
                          {msg}
                        </Alert>
                      </Box>
                      :
                      null
                  }

                  <Stack>
                    <Box
                      sx={{
                        width: "100%",
                        justifyContent: "center",
                        alignContent: "center",
                        display: "flex"
                      }}
                    >
                      <Button
                        tabIndex={0}
                        aria-label='Submit Parameters'
                        type='submit'
                        variant="contained"
                        sx={{
                          borderRadius: 3,
                          backgroundColor: themeFormat("colorButton",theme),
                          justifyContent: "center",
                          marginTop: 2,
                        }}
                      >
                        <Typography
                          component="span"
                          variant={themeFormat("textButton",theme)}
                          sx={{
                            fontFamily: themeFormat("buttonFontFamily",theme),
                            fontWeight: themeFormat("buttonFontWeight",theme)
                          }}
                        >
                          Submit
                        </Typography>
                      </Button>
                    </Box>
                  </Stack>
                </form>
                {
                  err == false && msg !== "" && runMode === "None" ?
                    null
                    :
                    <>
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
                          variant={themeFormat("textSize",theme)}
                          component="p"
                          sx={{
                            fontFamily: themeFormat("textFontFamily",theme),
                            fontWeight: themeFormat("textFontWeight",theme),
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
                          aria-label='Go back and set other backend and algorithm'
                          onClick={clearData}
                          variant="contained"
                          sx={{
                            borderRadius: 3,
                            backgroundColor: themeFormat("colorButton",theme),
                            justifyContent: "center",
                            marginTop: 1,
                          }}
                        >
                          <Typography
                            component="span"
                            variant={themeFormat("textButton",theme)}
                            sx={{
                              fontFamily: themeFormat("buttonFontFamily",theme),
                              fontWeight: themeFormat("buttonFontWeight",theme)
                            }}
                          >
                            Go back
                          </Typography>
                        </Button>
                      </Box>
                    </>
                }
              </Stack>
            </Box>
          </>
          :
          null
      }
      {
        err == false && msg !== "" && runMode === "None" ?
          <>
            <Box
              sx={{
                width: "100%",
                justifyContent: "center",
                alignContent: "center",
                display: "flex",
                marginTop: 4,
              }}>
              <Stack
                sx={{
                  width: "40%",
                }}>
                <Grid container spacing={1}>
                  <Grid item xs={12} sm={12} md={6}>
                    <Box
                      sx={{
                        justifyContent: "center",
                        display: "flex",
                      }}>
                      <Button
                        tabIndex={0}
                        aria-label='Run Simple Execution'
                        onClick={runNormal}
                        variant="contained"
                        sx={{
                          borderRadius: 3,
                          backgroundColor: themeFormat("colorButton",theme),
                          justifyContent: "center",
                          marginTop: 2,
                        }}
                      >
                        <Typography
                          component="span"
                          variant={themeFormat("textButton",theme)}
                          sx={{
                            fontFamily: themeFormat("buttonFontFamily",theme),
                            fontWeight: themeFormat("buttonFontWeight",theme)
                          }}
                        >
                          Simple Execution
                        </Typography>
                      </Button>
                    </Box>
                  </Grid>
                  <Grid item xs={12} sm={12} md={6}>
                    <Box
                      sx={{
                        justifyContent: "center",
                        display: "flex",
                      }}>
                      <Button
                        tabIndex={0}
                        aria-label='Run Experimental Mode'
                        onClick={runExperimental}
                        variant="contained"
                        sx={{
                          borderRadius: 3,
                          backgroundColor: themeFormat("colorButton",theme),
                          justifyContent: "center",
                          marginTop: 2,
                        }}
                      >
                        <Typography
                          component="span"
                          variant={themeFormat("textButton",theme)}
                          sx={{
                            fontFamily: themeFormat("buttonFontFamily",theme),
                            fontWeight: themeFormat("buttonFontWeight",theme)
                          }}
                        >
                          Experimental Mode
                        </Typography>
                      </Button>
                    </Box>
                  </Grid>
                </Grid>
              </Stack>
            </Box>
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
                variant={themeFormat("textSize",theme)}
                component="p"
                sx={{
                  fontFamily: themeFormat("textFontFamily",theme),
                  fontWeight: themeFormat("textFontWeight",theme),
                  marginTop: 2,
                  marginBottom: 2,
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
                aria-label='Go back and set other backend and algorithm'
                onClick={clearData}
                variant="contained"
                sx={{
                  borderRadius: 3,
                  backgroundColor: themeFormat("colorButton",theme),
                  justifyContent: "center",
                  marginTop: 2,
                }}
              >
                <Typography
                  component="span"
                  variant={themeFormat("textButton",theme)}
                  sx={{
                    fontFamily: themeFormat("buttonFontFamily",theme),
                    fontWeight: themeFormat("buttonFontWeight",theme)
                  }}
                >
                  Go back
                </Typography>
              </Button>
            </Box>
            <Box
              sx={{
                padding: "2%",
                marginTop: "2%",
              }}
            >
              <Accordion
                sx={{
                  borderRadius: 2,
                  padding: "2%",
                  bgcolor: theme.palette.mode === 'dark' ? themeFormat("colorTarjeta",theme) : themeFormat("colorTrajetaLight",theme),
                }}>
                <AccordionSummary
                  expandIcon={<ExpandMoreIcon />}
                  aria-controls="panel1a-content"
                  id="panel1a-header"
                >
                  <Typography
                    tabIndex={0}
                    justifyContent="left"
                    variant={themeFormat("textSize",theme)}
                    component="p"
                    sx={{
                      fontFamily: themeFormat("textFontFamily",theme),
                      fontWeight: themeFormat("textFontWeight",theme),
                      marginLeft: "1em"
                    }}
                  >
                    What is the difference between the Simple Execution and the Experimental Mode?
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
                      justifyContent="left"
                      variant={themeFormat("textSize",theme)}
                      component="p"
                      sx={{
                        fontFamily: themeFormat("textFontFamily",theme),
                        fontWeight: themeFormat("textFontWeight",theme),
                        marginLeft: "1em"
                      }}
                    >
                      Performing the simple execution of an algorithm refers to running it only once, obtaining
                      the result and a graphical representation of the circuit.
                      <br></br>
                      <br></br>
                      The experimental mode allows to run the algorithm several times to observe its behavior
                      represented in a generated histogram.
                    </Typography>
                  </Box>
                </AccordionDetails>
              </Accordion>
            </Box>
          </>
          :
          null
      }
    </Box >
  );
}

export default RunAlgorithmsForm2;
