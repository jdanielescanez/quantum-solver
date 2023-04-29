//redux-react 
import React from 'react';
import { useDispatch, useSelector } from 'react-redux';

//MUI imports
import Box from '@mui/material/Box';
import Grid from '@mui/material/Grid';
import Typography from '@mui/material/Typography';
import Button from '@mui/material/Button';
import FormControl from '@mui/material/FormControl';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import Select from '@mui/material/Select';;
import { useTheme } from '@mui/material';

//Fuctions
import { colorTokens } from '../Redux/reducers/ThemeFunctions/colorsTokensPallete';

//import actions
import {
  setCurrentBackend,
  setCurrentAlgorithm,
} from '../Redux/actions/setBackendAlgorithmParams';

const RunAlgorithmsForm1 = ({ allBackends, allAlgorithms }: any): any => {
  const { token } = useSelector((state: any) => state.login_reducer)

  const dispatch = useDispatch();

  const theme = useTheme();
  const colorButton = colorTokens(theme.palette.mode).blueAccent[500];

  const [backend, setBackend] = React.useState('');
  const [algorithm, setAlgorithm] = React.useState('');

  const handleChangeBackend = (event: any) => {
    setBackend(event.target.value);
  };

  const handleAlgorithm = (event: any) => {
    setAlgorithm(event.target.value);
  };

  const setAllData = async (e: any) => {
    e.preventDefault();
    dispatch(setCurrentBackend(token, backend));
    dispatch(setCurrentAlgorithm(token, Number(algorithm)));
  }

  return (
    <Box
      sx={{
        width: "100%",
        margin: "0 auto",
        padding: "0 10%",
      }}
    >
      <form className="registerForm" onSubmit={setAllData}>
        <Grid container
          rowSpacing={4}
          columnSpacing={{ xs: 1, sm: 2, md: 3 }}
          sx={{
            justifyContent: "center",
            alignContent: "center",
            alignItems: "center",
            width: "100%",
            margin: "0 auto",
            padding: "1em",
          }}>
          <Grid item xs={12} sm={4}>
            <Typography
              variant="h3"
              component="p"
              sx={{
                fontFamily: '"Helvetica Neue"',
                fontWeight: "bold"
              }}
            >
              Select backend:
            </Typography>
          </Grid>
          <Grid item xs={12} sm={8}>
            <FormControl
              id="backendid"
              component="div"
              aria-required="true"
              required
              fullWidth>
              <InputLabel
                id="demo-simple-select-label"
                color={theme.palette.mode === "dark" ? "secondary" : "primary"}
                sx={{
                  width: "100%",
                  display: "flex",
                }}
              >
                <Typography
                  component="span"
                  sx={{
                    fontFamily: '"Helvetica Neue"',
                    fontWeight: "italic"
                  }}
                >
                  Select backend
                </Typography>
              </InputLabel>
              <Select
                labelId="demo-simple-select-label"
                id="demo-simple-select"
                value={backend}
                label="Select BackEnd"
                onChange={handleChangeBackend}
                sx={{
                  width: "100%",
                }}
              >
                {
                  allBackends.map((backend: any, i: number) => {
                    return (
                      <MenuItem
                        key={"backend" + i}
                        tabIndex={0}
                        aria-label={backend.name}
                        value={backend.name}>
                        <Typography
                          sx={{
                            fontFamily: '"Helvetica Neue"',
                            fontWeight: "italic"
                          }}
                        >
                          name: {backend.name}, qubits: {backend.n_qubits}, shots: {backend.n_shots}, queue: {backend.jobs_in_queue}
                        </Typography>
                      </MenuItem>)
                  })
                }
              </Select>
            </FormControl>
          </Grid>
          <Grid item xs={12} sm={4}>
            <Typography
              variant="h3"
              component="p"
              sx={{
                fontFamily: '"Helvetica Neue"',
                fontWeight: "bold"
              }}
            >
              Select Algorithm:
            </Typography>
          </Grid>
          <Grid item xs={12} sm={8}>
            <FormControl
              component="div"
              aria-required="true"
              required
              fullWidth
            >
              <InputLabel
                id="demo-simple-select-label-2"
                color={theme.palette.mode === "dark" ? "secondary" : "primary"}
                sx={{
                  width: "100%",
                  display: "flex",
                }}
              >
                <Typography
                  component="span"
                  sx={{
                    fontFamily: '"Helvetica Neue"',
                    fontWeight: "italic"
                  }}
                >
                  Select Algorithm
                </Typography>
              </InputLabel>
              <Select
                labelId="demo-simple-select-label-2"
                id="demo-simple-select-2"
                value={algorithm}
                label="Select Algorithm"
                onChange={handleAlgorithm}
                sx={{
                  width: "100%",
                }}
              >
                {
                  allAlgorithms.map((algorithms: any, i: number) => {
                    return (
                      <MenuItem
                        key={"Algorithm" + i}
                        tabIndex={0}
                        aria-label={algorithms.name}
                        value={algorithms.id}>
                        <Typography
                          sx={{
                            fontFamily: '"Helvetica Neue"',
                            fontWeight: "italic"
                          }}
                        >
                          {algorithms.name}
                        </Typography>
                      </MenuItem>
                    )
                  })
                }
              </Select>
            </FormControl>
          </Grid>
        </Grid>
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
            <Typography
              component="span"
              sx={{
                fontFamily: '"Helvetica Neue"',
                fontWeight: "bold"
              }}
            >
              Set backend and algorithm
            </Typography>
          </Button>
        </Box>
      </form >
    </Box >
  );
}

export default RunAlgorithmsForm1;