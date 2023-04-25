//redux-react 
import React from 'react';
import { useDispatch, useSelector } from 'react-redux';

//MUI imports
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import TextField from '@mui/material/TextField';
import FormControl from '@mui/material/FormControl';
import Stack from '@mui/material/Stack';
import Button from '@mui/material/Button';
import Grid from '@mui/material/Grid';
import Alert from '@mui/material/Alert';
import { useTheme } from '@mui/material';

//Fuctions
import { colorTokens } from '../Redux/reducers/ThemeFunctions/colorsTokensPallete';

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
  const colorButton = colorTokens(theme.palette.mode).blueAccent[500];

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
                variant="h3"
                component="p"
                sx={{
                  fontFamily: '"Helvetica Neue"',
                  fontWeight: "bold"
                }}>
                Set Parameters:
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
                            variant="body1"
                            component="p"
                            sx={{
                              fontFamily: '"Helvetica Neue"',
                              fontWeight: "italic",
                              marginTop: 1,
                              marginBottom: 3,
                            }}>
                            Insert param {i + 1} :
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
                            }}
                          />
                        </div>
                      );
                    })
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
                        aria-label='Set Params'
                        type='submit'
                        variant="contained"
                        sx={{
                          borderRadius: 3,
                          backgroundColor: colorButton,
                          justifyContent: "center",
                          marginTop: 2,
                        }}
                      >
                        <Typography sx={{ fontFamily: '"Helvetica Neue"', fontWeight: "bold" }}>
                          Set Params
                        </Typography>
                      </Button>
                    </Box>
                  </Stack>

                </form>

              </Stack>
            </Box>
          </>
          :
          null
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
              variant="filled"
              sx={{
                fontFamily: '"Helvetica Neue"',
                fontWeight: "bold",

              }}
            >
              {msg}</Alert>
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
              variant="filled"
              sx={{
                fontFamily: '"Helvetica Neue"',
                fontWeight: "bold",
              }}
            >
              {msg}</Alert>
          </Box>
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
                display: "flex"
              }}
            >
              <Typography
                tabIndex={0}
                variant="body1"
                component="p"
                sx={{
                  fontFamily: '"Helvetica Neue"',
                  fontWeight: "italic",
                  marginTop: 2,
                  marginBottom: 2,
                }}>
                OR
              </Typography>
            </Box>

            <Grid container spacing={{ xs: 2, md: 3 }} columns={{ xs: 4, sm: 8, md: 12 }}>
              <Grid item xs={2} sm={4} md={4} >
                <Box
                  sx={{
                    justifyContent: "center",
                    alignContent: "center",
                    display: "flex"
                  }}
                >
                  <Button
                    tabIndex={0}
                    aria-label='Set other backend and algorithm'
                    onClick={clearData}
                    variant="contained"
                    sx={{
                      width: "100%",
                      borderRadius: 3,
                      backgroundColor: colorButton,
                      justifyContent: "center",
                      marginTop: 2,
                    }}
                  >
                    <Typography sx={{ fontFamily: '"Helvetica Neue"', fontWeight: "bold" }}>
                      Set other backend and algorithm
                    </Typography>
                  </Button>
                </Box>
              </Grid>
              <Grid item xs={2} sm={4} md={4}>
                <Box
                  sx={{
                    justifyContent: "center",
                    alignContent: "center",
                    display: "flex"
                  }}
                >
                  <Button
                    tabIndex={0}
                    aria-label='Set other backend and algorithm'
                    onClick={runNormal}
                    variant="contained"
                    sx={{
                      width: "100%",
                      borderRadius: 3,
                      backgroundColor: colorButton,
                      justifyContent: "center",
                      marginTop: 2,
                    }}
                  >
                    <Typography sx={{ fontFamily: '"Helvetica Neue"', fontWeight: "bold" }}>
                      Run QuantumSolver
                    </Typography>
                  </Button>
                </Box>
              </Grid>
              <Grid item xs={2} sm={4} md={4}>
                <Box
                  sx={{
                    justifyContent: "center",
                    alignContent: "center",
                    display: "flex"
                  }}
                >
                  <Button
                    tabIndex={0}
                    aria-label='Set other backend and algorithm'
                    onClick={runExperimental}
                    variant="contained"
                    sx={{
                      width: "100%",
                      borderRadius: 3,
                      backgroundColor: colorButton,
                      justifyContent: "center",
                      marginTop: 2,
                    }}
                  >
                    <Typography sx={{ fontFamily: '"Helvetica Neue"', fontWeight: "bold" }}>
                      Run QuantumSolver Experimental Mode
                    </Typography>
                  </Button>
                </Box>
              </Grid>
            </Grid>
          </>
          :
          null
      }
    </Box >
  );
}

export default RunAlgorithmsForm2;
