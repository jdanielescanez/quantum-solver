// MUI imports
import Card from '@mui/material/Card';
import CardMedia from '@mui/material/CardMedia';
import CardContent from '@mui/material/CardContent';
import CardActions from '@mui/material/CardActions';
import IconButton from '@mui/material/IconButton';
import Typography from '@mui/material/Typography';
import { Box, Link as linkMui } from '@mui/material';
import { useTheme } from '@mui/material'

// Fuctions
import { themeFormat } from '../Redux/reducers/ThemeFunctions/personalizedColorsAndFounts';

//icons 
import LinkedInIcon from '@mui/icons-material/LinkedIn';
import TwitterIcon from '@mui/icons-material/Twitter';
import EmailIcon from '@mui/icons-material/Email';


// types
type PeopleCardProps = {
  name: string,
  position: string,
  photo: string,
  socialMedia: {
    linkedin: string,
    twitter: string,
    mail: string,
  },
  key: number,
}

export const PeopleCard = ({ name, position, photo, socialMedia }: PeopleCardProps): any => {
  const theme = useTheme();

  return (
    <Box>
      <Card
        color={theme.palette.mode === 'dark' ? themeFormat("colorTarjeta",theme)  : themeFormat("colorTrajetaLight",theme)}
        elevation={5}
        sx={{
          Height: "400px",
          minHeight: "400px",
          borderRadius: "5%",
        }}
      >
        <Box
          sx={{
            display: "flex",
            justifyContent: "center",
            alignContent: "center",
            alignItems: "center",
          }}>
          <CardMedia
            component="img"
            tabIndex={0}
            sx={{
              height: "auto",
              width: "auto",
              maxHeight: "350px",
              maxWidth: "200px",
              borderRadius: "10px",
              margin: "10px",
              display: "flex",
              justifyContent: "center",
            }}
            image={photo}
            alt={name + "'s photo"}
          />
        </Box>
        <CardContent>
          <Typography
            tabIndex={0}
            gutterBottom
            variant={themeFormat("titleh5",theme)}
            component="p"
            sx={{
              fontFamily: themeFormat("titleFontFamily",theme),
              fontWeight: themeFormat("titleFontWeight",theme),
              alignContent: "center",
              justifyContent: "center",
              display: "flex",
            }}
          >
            {name}
          </Typography>
          <Typography
            tabIndex={0}
            variant={themeFormat("textSize",theme)}
            component="p"
            color="text.secondary"
            sx={{
              fontFamily: themeFormat("textFontFamily",theme),
              fontWeight: themeFormat("textFontWeight",theme),
              alignContent: "center",
              justifyContent: "center",
              display: "flex",
            }}
          >
            {position}
          </Typography>
        </CardContent>
        <CardActions
          sx={{
            justifyContent: "center",
            alignContent: "center",
            alignItems: "center",
            display: "flex",
          }}>
          {
            socialMedia.linkedin !== "" ?
              <IconButton
                aria-label="Link to linkedin"
                size="small"
                component={linkMui} href={socialMedia.linkedin} target="_blank"
              >
                <LinkedInIcon />
              </IconButton>
              :
              null
          }
          {
            socialMedia.twitter !== "" ?
              <IconButton
                aria-label="Link to twitter"
                size="small"
                component={linkMui} href={socialMedia.twitter} target="_blank"
              >
                <TwitterIcon />
              </IconButton>
              :
              null
          }
          {
            socialMedia.mail !== "" ?
              <IconButton
                aria-label="Link to email"
                size="small"
                component={linkMui} href={"mailto:" + socialMedia.mail} target="_blank"
              >
                <EmailIcon />
              </IconButton>
              :
              null
          }
        </CardActions>
      </Card>
    </Box>
  );
}
