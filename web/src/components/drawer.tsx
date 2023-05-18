// React - Redux import
import { useDispatch, useSelector } from 'react-redux';
import { Link } from 'react-router-dom';

// MUI imports
import { styled, useTheme } from '@mui/material/styles';
import Drawer from '@mui/material/Drawer';
import List from '@mui/material/List';
import Divider from '@mui/material/Divider';
import IconButton from '@mui/material/IconButton';
import ChevronLeftIcon from '@mui/icons-material/ChevronLeft';
import ChevronRightIcon from '@mui/icons-material/ChevronRight';
import ListItem from '@mui/material/ListItem';
import ListItemButton from '@mui/material/ListItemButton';
import ListItemIcon from '@mui/material/ListItemIcon';
import ListItemText from '@mui/material/ListItemText';
import { Link as linkMui } from '@mui/material';


//import icons
import HomeIcon from '@mui/icons-material/Home';
import AccountCircleIcon from '@mui/icons-material/AccountCircle';
import BusinessCenterIcon from '@mui/icons-material/BusinessCenter';
import SettingsIcon from '@mui/icons-material/Settings';
import TouchAppIcon from '@mui/icons-material/TouchApp';
import PeopleAltIcon from '@mui/icons-material/PeopleAlt';
import GitHubIcon from '@mui/icons-material/GitHub';

//action
import setDrawer from '../Redux/actions/setDrawerActions';

// fuction
import { themeFormat } from '../Redux/reducers/ThemeFunctions/personalizedColorsAndFounts';

// Drawer width
const drawerWidth = 240;

// Mui Styled components
const DrawerHeader = styled('div')(({ theme }) => ({
  display: 'flex',
  alignItems: 'center',
  padding: theme.spacing(0, 1),
  // necessary for content to be below app bar
  ...theme.mixins.toolbar,
  justifyContent: 'flex-end',
}));


const DrawerContent = () => {
  const theme = useTheme();
  const dispatch = useDispatch();

  const open = useSelector((state: any) => state.drawer_reducer.open);

  return (
    <Drawer
      sx={{
        width: drawerWidth,
        flexShrink: 0,
        '& .MuiDrawer-paper': {
          width: drawerWidth,
          boxSizing: 'border-box',
        },
      }}
      variant="persistent"
      anchor="left"
      open={open}
    >
      <DrawerHeader>
        <IconButton
          aria-label="close drawer"
          onClick={() => dispatch(setDrawer(false))}>
          {theme.direction === 'ltr' ? <ChevronLeftIcon /> : <ChevronRightIcon />}
        </IconButton>
      </DrawerHeader>
      <Divider />
      <List>
        <ListItem disablePadding>
          <ListItemButton
            aria-label="Link to Home page"
            component={Link} to='/'
            >
            <ListItemIcon>
              <HomeIcon />
            </ListItemIcon>
            <ListItemText
              primary="Home page"
              primaryTypographyProps={{
                fontFamily: themeFormat("titleFontFamily",theme),
                fontWeight: themeFormat("titleFontWeight",theme),
                fontSize: themeFormat("listDrawerFontSize",theme),
              }}
            />
          </ListItemButton>
        </ListItem>

        <ListItem disablePadding>
          <ListItemButton
            tabIndex={0}
            aria-label="Link to Login page"
            component={Link} to='/login'>
            <ListItemIcon>
              <AccountCircleIcon />
            </ListItemIcon>
            <ListItemText
              primary="Login page"
              primaryTypographyProps={{
                fontFamily: themeFormat("titleFontFamily",theme),
                fontWeight: themeFormat("titleFontWeight",theme),
                fontSize: themeFormat("listDrawerFontSize",theme),
              }} />
          </ListItemButton>
        </ListItem>

        <ListItem disablePadding>
          <ListItemButton
            tabIndex={0}
            aria-label="Link to Information Algorithms page"
            component={Link} to='/algorithms'>
            <ListItemIcon>
              <BusinessCenterIcon />
            </ListItemIcon>
            <ListItemText
              primary="Algorithms information"
              primaryTypographyProps={{
                fontFamily: themeFormat("titleFontFamily",theme),
                fontWeight: themeFormat("titleFontWeight",theme),
                fontSize: themeFormat("listDrawerFontSize",theme),
              }}
            />
          </ListItemButton>
        </ListItem>

        <ListItem disablePadding>
          <ListItemButton
            tabIndex={0}
            aria-label="Link to Run Algorithms page"
            component={Link} to='/algorithmsRun'>
            <ListItemIcon>
              <SettingsIcon />
            </ListItemIcon>
            <ListItemText
              primary="Run algorithms"
              primaryTypographyProps={{
                fontFamily: themeFormat("titleFontFamily",theme),
                fontWeight: themeFormat("titleFontWeight",theme),
                fontSize: themeFormat("listDrawerFontSize",theme),
              }} />
          </ListItemButton>
        </ListItem>
      </List>
      <Divider />
      <List>
        <ListItem disablePadding>
          <ListItemButton
            tabIndex={0}
            aria-label="link to About us page"
            component={Link} to='/about'>
            <ListItemIcon>
              <PeopleAltIcon />
            </ListItemIcon>
            <ListItemText
              primary="About us"
              primaryTypographyProps={{
                fontFamily: themeFormat("titleFontFamily",theme),
                fontWeight: themeFormat("titleFontWeight",theme),
                fontSize: themeFormat("listDrawerFontSize",theme),
              }} />
          </ListItemButton>
        </ListItem>

        <ListItem disablePadding>
          <ListItemButton
            tabIndex={0}
            aria-label="link to Accessibility statement page"
            component={Link} to='/accessibility'>
            <ListItemIcon>
              <TouchAppIcon />
            </ListItemIcon>
            <ListItemText
              primary="Accessibility statement"
              primaryTypographyProps={{
                fontFamily: themeFormat("titleFontFamily",theme),
                fontWeight: themeFormat("titleFontWeight",theme),
                fontSize: themeFormat("listDrawerFontSize",theme),
              }} />
          </ListItemButton>
        </ListItem>

        <ListItem disablePadding>
          <ListItemButton
            tabIndex={0}
            aria-label="link to Github Page"
            component={linkMui} href='https://github.com/alu0101238944/quantum-solver' target="_blank"
          >
            <ListItemIcon>
              <GitHubIcon />
            </ListItemIcon>
            <ListItemText
              primary="Github repository"
              primaryTypographyProps={{
                fontFamily: themeFormat("titleFontFamily",theme),
                fontWeight: themeFormat("titleFontWeight",theme),
                fontSize: themeFormat("listDrawerFontSize",theme),
              }} />
          </ListItemButton>
        </ListItem>
      </List>
    </Drawer>
  );
};

export default DrawerContent;