//redux-react 
import { useDispatch, useSelector } from 'react-redux';

//MUI imports
import Box from '@mui/material/Box';
import Grid from '@mui/material/Grid';
import Typography from '@mui/material/Typography';
import Button from '@mui/material/Button';
import FormControl from '@mui/material/FormControl';
import InputLabel from '@mui/material/InputLabel';
import Select from '@mui/material/Select';
import MenuItem from '@mui/material/MenuItem';
import { useTheme } from '@mui/material';

//Fuctions
import { colorTokens } from '../Redux/reducers/ThemeFunctions/colorsTokensPallete';

const RunAlgorithmsForm = ({ allBackends, allAlgorithms }: any) => {
  console.log("RunAlgorithmsForm")
  console.log("all Backends", allAlgorithms)

  const theme = useTheme();
  const colorButton = colorTokens(theme.palette.mode).blueAccent[500];


  const currentBackend = useSelector((state: any) => state.runAlgorithms_reducer.currentBackend);
  const currentAlgorithm = useSelector((state: any) => state.runAlgorithms_reducer.currentAlgorithm);
  //const currentParams = useSelector((state: any) => state.runAlgorithms_reducer.currentParams);

  const handleSelection = (event: any) => {
    // event.preventDefault();
    //dispatch(setCurrentBackend(currentBackend));
    //dispatch(setCurrentAlgorithm(currentAlgorithm));
    //dispatch(setCurrentParams(currentParams));
  };

  const handleChangeBackend = (event: any) => {
    //setCurrentBackend(event.target.value as string);
  };

  //const [setCurrentAlgorithm] = useState('');
  const handleChangeAlgorithm = (event: any) => {
    //setCurrentAlgorithm(event.target.value as string);
  };

  return (
    <Box
      sx={{
        width: "100%",
        margin: "0 auto",
        padding: "0 10%",
        
      }}
      >
      <form className="registerForm" onSubmit={handleSelection}>
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
          <Grid item xs={4}>
            <Typography
              tabIndex={0}
              sx={{ fontFamily: '"Helvetica Neue"', fontWeight: "italic" }}>
              Select backend:
            </Typography>
          </Grid>
          <Grid item xs={8}>
            <FormControl fullWidth>
              <InputLabel
                aria-label='Select Backend'
                id="demo-simple-select-label"
                sx={{
                  width: "100%",
                  display: "flex",
                }}>Select the backend</InputLabel>
              <Select
                labelId="demo-simple-select-label"
                id="demo-simple-select"
                value={currentBackend}
                label="Select the backend"
                onChange={handleChangeBackend}
                sx={{
                  width: "100%",
                }}
              >
                <MenuItem value="">
                  <em>None</em>
                </MenuItem>
                {
                  allBackends.map((backend: any) => {
                    return (
                      <MenuItem
                        tabIndex={0}
                        aria-label={backend.name}
                        value={backend.name}> qubits: {backend.n_qubits}, shots: {backend.n_shots}, queue:{backend.jobs_in_queue} </MenuItem>
                    )
                  })
                }
              </Select>
            </FormControl>
          </Grid>
          <Grid item xs={4}>
            <Typography
              tabIndex={0}
              sx={{ fontFamily: '"Helvetica Neue"', fontWeight: "italic" }}>
              Select algorithm:
            </Typography>
          </Grid>
          <Grid item xs={8}>
            <FormControl fullWidth>
              <InputLabel
                aria-label='Select Algorithm'
                id="demo-simple-select-label"
                sx={{
                  width: "100%",
                  display: "flex",
                }}>Select the algorithm</InputLabel>
              <Select
                labelId="demo-simple-select-label"
                id="demo-simple-select"
                value={currentAlgorithm}
                label="Select the algorithm"
                onChange={handleChangeAlgorithm}
                sx={{
                  width: "100%",
                }}
              >
                <MenuItem value="">
                  <em>None</em>
                </MenuItem>
                {
                  allAlgorithms.map((algorithms: any) => {
                    return (
                      <MenuItem
                        tabIndex={0}
                        aria-label={algorithms.name}
                        value={algorithms.name}>{algorithms.name}</MenuItem>
                    )
                  })
                }
              </Select>
            </FormControl>
          </Grid>
        </Grid>
        <Box
          sx={{
            display: "flex",
            justifyContent: "center",
            alignContent: "center",
          }}
          >
          <Button
            tabIndex={0}
            aria-label='submit information'
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
              submit
            </Typography>
          </Button>
        </Box>
      </form>
    </ Box>
  );
}

export default RunAlgorithmsForm;
