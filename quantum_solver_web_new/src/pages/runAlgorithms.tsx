//import React-Redux
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

// components Import 
import RunAlgorithmsForm from '../components/runAlgorithmsForm'

const getAllData = async (dispatch: any, token: string) => {
  await dispatch(getBackendAlgorithmsParams(token))
  await dispatch(getBackendData(token))
  await dispatch(getAlgorithmData(token))
}


export const RunAlgorithms = () => {
  const dispatch = useDispatch();
  const theme = useTheme();
  const colorButton = colorTokens(theme.palette.mode).blueAccent[500];
  const navigate = useNavigate()
  const { token } = useSelector((state: any) => state.login_reducer)

  const allBackends = useSelector((state: any) => state.runAlgorithms_reducer.backendData);
  const allAlgorithms = useSelector((state: any) => state.runAlgorithms_reducer.algorithmsData);
  const allParams = useSelector((state: any) => state.runAlgorithms_reducer.paramsData);



  if (token !== "" && allBackends === "" && allAlgorithms === "") {
    getAllData(dispatch, token)
  }

  return (
    <div className="runAlgorithms">
      <Container
        maxWidth="xl"
        sx={{
          marginY: 5,
          marginBottom: "2em",
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
                width:"100%"
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
                  component="h1"
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
                        <Typography sx={{ fontFamily: '"Helvetica Neue"', fontWeight: "bold" }}>
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
                      <Alert severity="warning" variant="filled">{"You need to be logged in to run algorithms "}</Alert>
                    </Box>
                  </>
                  :
                  null
              }
              {
                token !== ""
                  && allBackends === "" && allAlgorithms === "" && allParams === "" ?
                  <>
                    <Typography sx={{ fontFamily: '"Helvetica Neue"', fontWeight: "bold" }}>
                      Loading...
                    </Typography>
                  </>
                  :
                  null
              }
              {
                token !== ""
                  && allBackends !== "None" && allAlgorithms !== "None" && allParams === "None" ?
                  < RunAlgorithmsForm allBackends={allBackends} allAlgorithms={allAlgorithms} />
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
