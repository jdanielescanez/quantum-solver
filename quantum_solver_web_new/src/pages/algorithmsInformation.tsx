//React - Redux
import { useDispatch, useSelector } from 'react-redux'
import { useNavigate } from 'react-router-dom'

// MUI imports
import Container from '@mui/material/Container'
import Paper from '@mui/material/Paper'
import Box from '@mui/material/Box'
import Typography from '@mui/material/Typography'
import Alert from '@mui/material/Alert'
import { useTheme } from '@mui/material'

// Fuctions
import { colorTokens } from '../Redux/reducers/ThemeFunctions/colorsTokensPallete';

//actions
import { getAlgorithms, clearAlgorithms } from '../Redux/actions/getAlgorithmActions'

// components
import { ListAlgorithm } from '../components/listOfAlgoritms'
import { Button, List } from '@mui/material'

const getAlgorithmsFunction = async (token: string, dispatch: any) => {
  await dispatch(getAlgorithms(token))
}

export const AlgorithmsInformation = () => {
  const theme = useTheme();
  const colorButton = colorTokens(theme.palette.mode).blueAccent[500];

  const dispatch = useDispatch()
  const navigate = useNavigate()

  const { token } = useSelector((state: any) => state.login_reducer)
  const { algorithmData } = useSelector((state: any) => state.getAlgorithms_reducer)

  if (algorithmData === "" && token !== "") {
    getAlgorithmsFunction(token, dispatch)
  }
  return (
    <div className="algorithmsInformation">
      <Container
        maxWidth="xl"
        sx={{
          marginY: 5,
          marginBottom: "2em",
          height: "100%",
          flexGrow: 0,
        }}>
        <Paper
          elevation={3}
          sx={{
            borderRadius: 10,
            margin: "auto",
            height: "100%",
            padding: "10%",
          }}>
          <Box
            sx={{
              padding: 2,
              justifyContent: "center",
              display: "flex",
            }}>
            <Typography
              tabIndex={0}
              variant="h2"
              component="h1"
              sx={{
                fontFamily: '"Helvetica Neue"',
                fontWeight: "bold"
              }}
            >
              Algorithms Information
            </Typography>
          </Box>
          {
            algorithmData === "" && token === "" ? (
              <Box
                sx={{
                  padding: 2,
                  justifyContent: "center",
                  display: "flex",
                }}>
                <Button
                  tabIndex={0}
                  aria-label='Go to login Button'
                  variant="contained"
                  sx={{
                    borderRadius: 3,
                    backgroundColor: colorButton,
                    justifyContent: "center",
                  }}
                  onClick={() =>
                    navigate("/login")
                  }
                >
                  Go to login
                </Button>
              </Box>
            ) : (
              null
            )
          }
          {token === "" ? (
            <Box
              sx={{
                padding: 2,
                justifyContent: "center",
                display: "flex",
              }}>
              <Alert severity="warning" variant="filled">{"You Need to be logged to see the algorithms information "}</Alert>
            </Box>
          ) : null}
          {algorithmData !== "" ? <ListAlgorithm listAlgorithm={algorithmData} /> : null}

          {
            algorithmData !== "" && token === "" ? (
              dispatch(clearAlgorithms())
            ) : (
              null
            )
          }

        </Paper>
      </Container>
    </div>
  )
}