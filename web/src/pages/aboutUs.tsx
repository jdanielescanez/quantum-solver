//MUI imports
import Container from '@mui/material/Container'
import Paper from '@mui/material/Paper'
import Box from '@mui/material/Box'
import Stack from '@mui/material/Stack'
import Typography from '@mui/material/Typography'
import { useTheme } from '@mui/material'


// Components
import { BreadCrumbsComponent } from '../components/breadCrumbs'
import { ListPeople } from '../components/listOfPeople'

// theme format
import { themeFormat } from '../Redux/reducers/ThemeFunctions/personalizedColorsAndFounts';

type PeopleCardProps = {
  name: string,
  position: string,
  photo: string,
  socialMedia: {
    linkedin: string,
    twitter: string,
    mail: string,
  },
}[]


const PeopleCardData: PeopleCardProps = [
  {
    name: "Daniel Escanez-Exposito",
    position: "CryptULL, University of La Laguna",
    photo: "teamPhotos/DanielEscanez.png",
    socialMedia: {
      linkedin: "https://www.linkedin.com/in/jdanielescanez/",
      twitter: "https://twitter.com/JDanielEscanez?t=pam5yC4VSvATKPMvvvvC2A&s=09",
      mail: "jdanielescanez@gmail.com",
    },
  },
  {
    name: "Pino Caballero-Gil",
    position: "CryptULL, University of La Laguna",
    photo: "teamPhotos/PinoCaballero.png",
    socialMedia: {
      linkedin: "https://www.linkedin.com/in/pino-caballero-gil-04444235/",
      twitter: "https://twitter.com/PinoCaballero",
      mail: "Pcaballe@ull.edu.es",
    },
  },
  {
    name: "Francisco Martin-Fernandez",
    position: "IBM Research",
    photo: "teamPhotos/FranciscoMartin.png",
    socialMedia: {
      linkedin: "https://www.linkedin.com/in/fmartinfdez",
      twitter: "https://www.linkedin.com/in/fmartinfdez",
      mail: "paco@ibm.com",
    },
  },
  {
    name: "Vlatko Marchan-Sekulic",
    position: "Student Computer Engineering at ULL",
    photo: "teamPhotos/Vlatko.png",
    socialMedia: {
      linkedin: "https://www.linkedin.com/in/vlatko-jesus-marchan-sekulic-ciberseguridad/",
      twitter: "",
      mail: "89vlatko@gmail.com",
    },
  },
  {
    name: "Andrea Hernandez-Martin",
    position: "Student Computer Engineering at ULL",
    photo: "teamPhotos/AndreaHernandez.png",
    socialMedia: {
      linkedin: "https://www.linkedin.com/in/andreahdezm/",
      twitter: "",
      mail: "andre280499@gmail.com",
    },
  },
]


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
                  align="center"
                  variant={themeFormat("titleh2",theme)}
                  component="h2"
                  sx={{
                    fontFamily: themeFormat("titleFontFamily",theme),
                    fontWeight: themeFormat("titleFontWeight",theme)
                  }}
                >
                  About us
                </Typography>
              </Box>

              <Box
                sx={{
                  justifyContent: "left",
                  display: "flex",
                  marginBottom: "2em",
                }}>
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
                  QuantumSolver is an initiative for democratizing quantum development
                  that started in early 2022 with the support of the Binter Cybersecurity
                  Chair of the University of La Laguna (ULL) and the Cryptology research group
                  of the same university (CryptULL).
                  <br />
                  <br />
                  The main developers of QuantumSolver are listed below:
                </Typography>
              </Box>

              <Box
                sx={{
                  justifyContent: "center",
                  display: "flex",
                  marginBottom: "1em",
                }}>
                <ListPeople listPeople={PeopleCardData} />
              </Box>
            </Stack>
          </Box>
        </Paper>
      </Container>
    </div>
  );
}