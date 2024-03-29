// MUI imports
import Paper from '@mui/material/Paper'
import Box from '@mui/material/Box'
import Typography from '@mui/material/Typography'
import Acordion from '@mui/material/Accordion'
import AccordionSummary from '@mui/material/AccordionSummary'
import AccordionDetails from '@mui/material/AccordionDetails'
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
import { useTheme } from '@mui/material'

// Fuctions
import { themeFormat } from '../Redux/reducers/ThemeFunctions/personalizedColorsAndFounts';


type AlgorithmCardProps = {
  algorithmName: string,
  description: string,
  parameters: [],
}


export const AlgorithmCard = ({ algorithmName, description, parameters }: AlgorithmCardProps) => {
  const theme = useTheme();
  return (
    <div >
      <Paper
        elevation={5}
        sx={{
          padding: 2,
          margin: 2,
          borderRadius: 10,
          bgcolor: theme.palette.mode === 'dark' ? themeFormat("colorTarjeta",theme) : themeFormat("colorTrajetaLight",theme),
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
            align="center"
            variant={themeFormat("titleh3",theme)}
            component="h2"
            sx={{
              fontFamily: themeFormat("titleFontFamily",theme),
              fontWeight: themeFormat("titleFontWeight",theme),
            }}
          >
            <b>Algorithms </b> {algorithmName}
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
            align="left"
            justifyContent="left"
            variant={themeFormat("textSize",theme)}
            component="p"
            sx={{
              fontFamily: themeFormat("textFontFamily",theme),
              fontWeight: themeFormat("textFontWeight",theme),
              marginLeft: "2em",
              marginRight: "2em"
            }}
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
            justifyContent="left"
            align="center"
            variant={themeFormat("titleh4",theme)}
            component="h2"
            sx={{
              fontFamily: themeFormat("titleFontFamily",theme),
              fontWeight: themeFormat("titleFontWeight",theme),
            }}
          >
            Parameters characteristics
          </Typography>
        </Box>
        <Box sx={{ marginLeft: "2em", marginRight: "2em", padding: "2%" }}>

          {parameters.map((parameter: any, i: number) => (
            <Acordion
              key={i.toString()}
              sx={{
                borderRadius: 2,
                padding: "2%",
                bgcolor: theme.palette.mode === 'dark' ? themeFormat("colorTarjeta",theme) : themeFormat("colorTarjeta",theme),
              }}>
              <AccordionSummary
                key={"AcordionSection" + i}
                expandIcon={<ExpandMoreIcon />}
                aria-controls="panel1a-content"
                id="panel1a-header">
                <Typography
                  variant={themeFormat("titleh6",theme)}
                  component="p"
                  justifyContent="left"
                  sx={{
                    fontFamily: themeFormat("textFontFamily",theme),
                    fontWeight: themeFormat("textFontWeight",theme),
                    marginLeft: "1em"
                  }}
                >
                  <b>Type: </b>{parameter.type}
                </Typography>
              </AccordionSummary>
              <AccordionDetails
                key={"AcordionSection" + i}>
                <Typography
                  tabIndex={0}
                  variant={themeFormat("textSize",theme)}
                  component="p"
                  justifyContent="left"
                  sx={{
                    fontFamily: themeFormat("textFontFamily",theme),
                    fontWeight: themeFormat("textFontWeight",theme),
                    marginLeft: "1em"
                  }}
                >
                  <b>Constraint: </b>{parameter.constraint}
                </Typography>
                <Typography
                  tabIndex={0}
                  variant={themeFormat("textSize",theme)}
                  component="p"
                  justifyContent="left"
                  sx={{
                    fontFamily: themeFormat("textFontFamily",theme),
                    fontWeight: themeFormat("textFontWeight",theme),
                    marginLeft: "1em"
                  }}
                >
                  <b>Description: </b>{parameter.description}
                </Typography>
              </AccordionDetails>
            </Acordion>
          ))}
        </Box>
      </Paper >
    </div>
  )
}
