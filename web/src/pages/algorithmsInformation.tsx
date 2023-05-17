//React - Redux
import { useDispatch, useSelector } from 'react-redux'
import { useNavigate } from 'react-router-dom'
import { Link } from 'react-router-dom';

// MUI imports
import Container from '@mui/material/Container'
import Paper from '@mui/material/Paper'
import Box from '@mui/material/Box'
import Typography from '@mui/material/Typography'
import Alert from '@mui/material/Alert'
import { useTheme } from '@mui/material'
import { Button, List } from '@mui/material'

// Fuctions
import { themeFormat } from '../Redux/reducers/ThemeFunctions/personalizedColorsAndFounts';

//actions
import { getAlgorithms, clearAlgorithms } from '../Redux/actions/getAlgorithmActions'

// components
import { ListAlgorithm } from '../components/listOfAlgoritms'
import { BreadCrumbsComponent } from '../components/breadCrumbs'

const getAlgorithmsFunction = async (token: string, dispatch: any) => {
  await dispatch(getAlgorithms(token))
}

export const AlgorithmsInformation = () => {
  const theme = useTheme();

  const dispatch = useDispatch()
  const navigate = useNavigate()

  const { token } = useSelector((state: any) => state.login_reducer)
  const { isToken } = useSelector((state: any) => state.login_reducer)
  const { algorithmData } = useSelector((state: any) => state.getAlgorithms_reducer)

  if (algorithmData === "" && isToken) {
    getAlgorithmsFunction(token, dispatch)
  }

  const routesAlgorithmInfo = ['/login', '/algorithms']

  return (
    <div className="algorithmsInformation">
      <BreadCrumbsComponent routes={routesAlgorithmInfo} />
      <Container
        maxWidth="xl"
        sx={{
          marginY: 1,
          marginBottom: "2em",
          height: "100%",
          flexGrow: 0,
          minHeight: "60vh",
        }}>
        <Paper
          elevation={3}
          sx={{
            borderRadius: 10,
            margin: "auto",
            height: "100%",
            padding: "2%",
          }}>
          <Box
            sx={{
              padding: 2,
              justifyContent: "center",
              display: "flex",
            }}>
            <Typography
              tabIndex={0}
              variant={themeFormat("titleh2",theme)}
              component="h2"
              sx={{
                fontFamily: themeFormat("titleFontFamily",theme),
                fontWeight: themeFormat("titleFontWeight",theme)
              }}
            >
              Algorithms Information
            </Typography>
          </Box>
          {
            algorithmData === "" && !isToken ? (
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
                    backgroundColor: themeFormat("colorButton",theme),
                    justifyContent: "center",
                  }}
                  onClick={() =>
                    navigate("/login")
                  }
                >
                  <Typography
                    component="span"
                    variant={themeFormat("textButton",theme)}
                    sx={{
                      fontFamily: themeFormat("buttonFontFamily",theme),
                      fontWeight: themeFormat("buttonFontWeight",theme)
                    }}
                  >
                    Go to login
                  </Typography>
                </Button>
              </Box>
            ) : (
              null
            )
          }
          {!isToken ? (
            <Box
              sx={{
                padding: 2,
                justifyContent: "center",
                display: "flex",
              }}>
              <Alert
                severity="warning"
                variant={themeFormat("alertVariant",theme)}
                sx={{
                  fontFamily: themeFormat("alertsFontFamily",theme),
                  fontWeight: themeFormat("alertsFontWeight",theme),
                  color: themeFormat("warning",theme),
                }}
              >
                {"You Need to be logged to see the algorithms information "}
              </Alert>
            </Box>
          ) : null}
          {
            algorithmData !== "" ?
              <>
                <Box
                  sx={{
                    padding: 2,
                    justifyContent: "center",
                    display: "flex",
                  }}>
                  <Typography
                    tabIndex={0}
                    variant={themeFormat("textSize",theme)}
                    component="p"
                    sx={{
                      fontFamily: themeFormat("textFontFamily",theme),
                      fontWeight: themeFormat("textFontWeight",theme)
                    }}
                  >
                    You can execute all of this algorithms in the section&nbsp;
                    <Typography
                      tabIndex={0}
                      aria-label="link to Run Algorithms page"
                      component={Link} to='/algorithmsRun'
                      variant={themeFormat("textSize",theme)}
                      color={themeFormat("colorLinks",theme)}
                      sx={{
                        textDecoration: themeFormat("linksDecoration",theme),
                        fontFamily: themeFormat("textFontFamily",theme),
                        fontWeight: themeFormat("linkFontWeight",theme),
                      }}
                    >
                      Run Algorithms
                    </Typography>
                  </Typography>
                </Box>
                <ListAlgorithm listAlgorithm={algorithmData} />
              </>
              :
              null}

          {
            algorithmData !== "" && !isToken ? (
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