//MUI imports
import Container from '@mui/material/Container'
import Paper from '@mui/material/Paper'
import Box from '@mui/material/Box'
import Stack from '@mui/material/Stack'
import Typography from '@mui/material/Typography'
import { useTheme } from '@mui/material'


// Components
import { BreadCrumbsComponent } from '../components/breadCrumbs'

// Fuctions
import { themeFormat } from '../Redux/reducers/ThemeFunctions/personalizedColorsAndFounts';


export const Accessibility = () => {

  const theme = useTheme();

  const routesAccessibility = ['/accessibility']

  return (
    <div className="Accessibility">
      <BreadCrumbsComponent routes={routesAccessibility} />
      <Container
        maxWidth="xl"
        sx={{
          marginY: 1,
          marginBottom: "2em",
          minHeight: "60vh",
        }}>
        <Paper
          elevation={3}
          sx={{
            padding: "2%",
            margin: 2,
            borderRadius: 10,
          }}>
          <Box
            sx={{
              padding: 2,
              justifyContent: "center",
              alignContent: "center",
              display: "flex",
              marginTop: "2em",
              marginBottom: "2em",
            }}>
            <Stack
              spacing={2}
              alignItems="center">
              <Box
                sx={{
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
                  Accessibility Statement for Quantum Solver website
                </Typography>
              </Box>
              <Typography
                tabIndex={0}
                align="left"
                variant={themeFormat("textSize",theme)}
                component="p"
                sx={{
                  fontFamily: themeFormat("textFontFamily",theme),
                  fontWeight: themeFormat("textFontWeight",theme)
                }}
              >
                The primary objective of developing the QuantumSolver open-source library was to make quantum computing accessible to the general public. To achieve this goal, we have created a website that is designed to be as user-friendly as possible, following the AA WCAG 2.1 standards for accessibility. These guidelines are a set of stable technical reference standards that consist of 12-13 guidelines grouped into four principles: perceivable, operable, understandable, and robust. Each guideline includes specific conformance criteria that can be tested and are classified into three levels: A, AA, and AAA. The AA WCAG 2.1 standards are an updated version of the WCAG 2.0 standards and include an additional 17 conformance criteria that must be considered.
              </Typography>

            </Stack>
          </Box>
        </Paper>
      </Container>
    </div>
  );
}