//MUI imports
import Container from '@mui/material/Container'
import Paper from '@mui/material/Paper'
import Box from '@mui/material/Box'
import Stack from '@mui/material/Stack'
import Typography from '@mui/material/Typography'
import { useTheme } from '@mui/material'


// Components
import { BreadCrumbsComponent } from '../components/breadCrumbs'


export const AboutUs = () => {
  const theme = useTheme();

  const routesAccessibility = ['/about']

  return (
    <div className="AboutUs">
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
            padding: 2,
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
                  variant="h2"
                  component="h2"
                  align="center"
                  sx={{ fontFamily: '"Helvetica Neue"', fontWeight: "bold" }}
                >
                  About us
                </Typography>
              </Box>
            </Stack>
          </Box>
        </Paper>
      </Container>
    </div>
  );
}