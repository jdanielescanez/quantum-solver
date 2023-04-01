

// MUI imports
import Paper from '@mui/material/Paper'
import Box from '@mui/material/Box'
import Typography from '@mui/material/Typography'
import Acordion from '@mui/material/Accordion'
import AccordionSummary from '@mui/material/AccordionSummary'
import AccordionDetails from '@mui/material/AccordionDetails'
import { useTheme } from '@mui/material'

// Fuctions
import { colorTokens } from '../Redux/reducers/ThemeFunctions/colorsTokensPallete';


type AlgorithmCardProps = {
  algorithmName: string,
  description: string,
  parameters: [],
}


export const AlgorithmCard = ({ algorithmName, description, parameters }: AlgorithmCardProps) => {
  const theme = useTheme();

  const colorTarjeta = colorTokens(theme.palette.mode).grey[800];
  const colorTrajetaLight = colorTokens(theme.palette.mode).grey[900];

  return (
    <Paper
      elevation={5}
      sx={{
        padding: 2,
        margin: 2,
        borderRadius: 10,
        bgcolor: theme.palette.mode === 'dark' ? colorTarjeta : colorTrajetaLight ,
      }}
    >
      <Box
        sx={{
          display: 'flex',
          justifyContent: 'center',
          alignItems: 'center',
          flexDirection: 'column',
          padding: 1,
        }}
      >
        <Typography
          tabIndex={0}
          variant="h4"
          component="h2"
          align="center"
          sx={{ fontFamily: '"Helvetica Neue"', fontWeight: "italic" }}
        >
          <b>algorithm: </b> {algorithmName}
        </Typography>
      </Box>
      <Box sx={{ marginLeft: "2em", marginRight: "2em" }}>
        <hr />
      </Box>
      <Box
        sx={{
          tabindex: 0,
          display: 'flex',
          justifyContent: 'center',
          alignItems: 'center',
          flexDirection: 'column',
          padding: 4,
        }}
      >
        <Typography
          tabIndex={0}
          variant="body1"
          component="p"
          align="justify"
          justifyContent="left"
          sx={{ fontFamily: '"Helvetica Neue"', fontWeight: "italic", marginLeft: "2em", marginRight: "2em" }}
        >
          {description}
        </Typography>
      </Box>
      <Box sx={{ marginLeft: "2em", marginRight: "2em" }}>
        <hr />
      </Box>
      <Box
        sx={{
          display: 'flex',
          justifyContent: 'center',
          alignItems: 'center',
          flexDirection: 'column',
          padding: 1,
        }}
      >
        <Typography
          tabIndex={0}
          variant="h5"
          component="h2"
          align="center"
          justifyContent="left"
          sx={{ fontFamily: '"Helvetica Neue"', fontWeight: "bold" }}
        >
          Parameters characteristics
        </Typography>
      </Box>
      <Box sx={{ marginLeft: "2em", marginRight: "2em", padding:"2%" }}>

        {parameters.map((parameter: any) => (
          <Acordion
            sx={{ 
              borderRadius: 2, 
              padding:"2%", 
              bgcolor: theme.palette.mode === 'dark' ? colorTarjeta : colorTrajetaLight,
              }}>
            <AccordionSummary>
              <Typography
                variant="body2"
                component="p"
                justifyContent="left"
                sx={{ fontFamily: '"Helvetica Neue"', fontWeight: "italic", marginLeft: "1em" }}>
                <b>Type: </b>{parameter.type}
              </Typography>
            </AccordionSummary>
            <AccordionDetails>
              <Typography
                tabIndex={0}
                variant="body2"
                component="p"
                justifyContent="left"
                sx={{ fontFamily: '"Helvetica Neue"', fontWeight: "italic", marginLeft: "1em" }}>
                <b>Constraint: </b>{parameter.constraint}
              </Typography>
              <Typography
                tabIndex={0}
                variant="body2"
                component="p"
                justifyContent="left"
                sx={{ fontFamily: '"Helvetica Neue"', fontWeight: "italic", marginLeft: "1em" }}>
                <b>Description: </b>{parameter.description}
              </Typography>
            </AccordionDetails>
          </Acordion>
        ))}
      </Box>
    </Paper >
  )
}
