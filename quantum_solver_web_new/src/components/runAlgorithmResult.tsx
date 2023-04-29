// React imports
import { useSelector, useDispatch } from 'react-redux';

// MUI imports
import Stack from '@mui/material/Stack';
import Typography from '@mui/material/Typography';
import Box from '@mui/material/Box';
import Accordion from '@mui/material/Accordion';
import AccordionSummary from '@mui/material/AccordionSummary';
import AccordionDetails from '@mui/material/AccordionDetails';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
import Card from '@mui/material/Card';
import CardMedia from '@mui/material/CardMedia';
import CardActionArea from '@mui/material/CardActionArea';
import Grid from '@mui/material/Grid';
import Button from '@mui/material/Button';
import { useTheme } from '@mui/material';

// fuction
import { colorTokens } from '../Redux/reducers/ThemeFunctions/colorsTokensPallete';

// import actions
import {
  clearBackendAlgorithmsParams
} from '../Redux/actions/getBackendAlgorithmParams';

// import actions
import {
  getResult,
  clearExecutionData,
} from '../Redux/actions/runActions';


export const RunAlgorithmsResult = () => {
  const theme = useTheme();

  //Data
  const { token } = useSelector((state: any) => state.login_reducer)
  const result = useSelector((state: any) => state.runAlgorithms_reducer.result);
  const current_backend = useSelector((state: any) => state.runAlgorithms_reducer.currentBackend.msg);
  const current_algorithm = useSelector((state: any) => state.runAlgorithms_reducer.currentAlgorithm.msg);
  const current_params = useSelector((state: any) => state.runAlgorithms_reducer.currentParams.msg);

  // Colors
  const colorTarjeta = colorTokens(theme.palette.mode).grey[800];
  const colorTrajetaLight = colorTokens(theme.palette.mode).grey[900];
  const colorButton = colorTokens(theme.palette.mode).blueAccent[500];
  const colorLinks = colorTokens(theme.palette.mode).grey[100];

  const dispatch = useDispatch();

  if (result === "") {
    dispatch(getResult(token));
  }

  // Data processing  
  const imageBase64 = 'data:image/png;base64,' + result.image_base64;
  const figure_name = 'figure-' + current_backend + '-' + current_algorithm + '-' + current_params + '.png';

  const clearData = (e: any) => {
    e.preventDefault();
    dispatch(clearBackendAlgorithmsParams());
  }

  const clearExecutionDataFunction = (e: any) => {
    e.preventDefault();
    dispatch(clearExecutionData());
  }

  const copyOutput = () => {
    navigator.clipboard.writeText(result.output);
  }


  return (
    <>
      <Stack
        spacing={2}>
        <Box
          sx={{
            display: 'flex',
            justifyContent: 'center',
            alignItems: 'center',
            marginTop: '2rem',
            marginBottom: '1rem',
          }}
        >
          <Typography
            tabIndex={0}
            variant="h3"
            component="p"
            sx={{
              fontFamily: '"Helvetica Neue"',
              fontWeight: "bold",
            }}>
            Run result:
          </Typography>
        </Box>
        <Box
          sx={{
            display: 'flex',
            justifyContent: 'center',
            alignItems: 'center',
            marginTop: '2rem',
            marginBottom: '2rem',
            maxWidth: "100%",
            maxHeight: "100%",
            padding: "2%",
            radius: "2%",
          }}
        >
          <Card>
            <CardActionArea>
              <CardMedia
                tabIndex={0}
                component="img"
                image={imageBase64}
                alt={"resulting figure after execution of the algorithm " + current_algorithm}
                sx={{
                  maxWidth: "100%",
                  maxHeight: "100%"
                }}
              />
            </CardActionArea>
          </Card>
        </Box>
        <Box
          sx={{
            display: 'flex',
            justifyContent: 'center',
            alignItems: 'center',
            marginTop: '2rem',
            marginBottom: '2rem',
          }}
        >
          <Typography
            tabIndex={0}
            variant="h4"
            component="a"
            download={figure_name}
            href={imageBase64}
            color={colorLinks}
            sx={{
              fontFamily: '"Helvetica Neue"',
              fontWeight: "italic",
            }}>
            Download figure here
          </Typography>
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
                Output
              </Typography>
            </AccordionSummary>
            <AccordionDetails>
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
                {result.output}
              </Typography>
            </AccordionDetails>
          </Accordion>
        </Box>
      </Stack>
      <Box
        sx={{
          width: "100%",
          justifyContent: "center",
          alignContent: "center",
          display: "flex",
          padding: "2%",
        }}
      >
        <Grid container spacing={{ xs: 2, md: 3 }} columns={{ xs: 4, sm: 8, md: 12 }}>
          <Grid item xs={12} sm={4} md={4} >
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
                <Typography
                  component="span"
                  sx={{
                    fontFamily: '"Helvetica Neue"',
                    fontWeight: "bold"
                  }}
                >
                  Set other backend and algorithm
                </Typography>
              </Button>
            </Box>
          </Grid>
          <Grid item xs={12} sm={4} md={4}>
            <Box
              sx={{
                justifyContent: "center",
                alignContent: "center",
                display: "flex"
              }}
            >
              <Button
                tabIndex={0}
                aria-label='Clear execution data'
                onClick={clearExecutionDataFunction}
                variant="contained"
                sx={{
                  width: "100%",
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
                  Clear execution data
                </Typography>
              </Button>
            </Box>
          </Grid>
          <Grid item xs={12} sm={4} md={4}>
            <Box
              sx={{
                justifyContent: "center",
                alignContent: "center",
                display: "flex"
              }}
            >
              <Button
                tabIndex={0}
                aria-label='Copy output to clipboard'
                onClick={copyOutput}
                variant="contained"
                sx={{
                  width: "100%",
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
                  Copy output to clipboard
                </Typography>
              </Button>
            </Box>
          </Grid>
        </Grid>
      </Box>
    </>
  )
}
