// React - Redux import
import { useDispatch, useSelector } from 'react-redux';

// MUI elements
import IconButton from '@mui/material/IconButton';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import MenuIcon from '@mui/icons-material/Menu';
import Typography from '@mui/material/Typography';
import { useTheme, styled } from '@mui/material';
import MuiAppBar, { AppBarProps as MuiAppBarProps } from '@mui/material/AppBar';

//action
import setDrawer from '../Redux/actions/setDrawerActions';

//icons
import LightModeOutlinedIcon from '@mui/icons-material/LightModeOutlined';
import DarkModeOutlinedICon from '@mui/icons-material/DarkModeOutlined';

// assets
import LightLogo from '../assets/LightLogo192.png';
import DarkLogo from '../assets/DarkLogo192.png';
import { set_theme_dark_action, set_theme_light_action } from '../Redux/actions/themeMode';

const drawerWidth = 240;

interface AppBarProps extends MuiAppBarProps {
  open?: boolean;
}

const AppBar = styled(MuiAppBar, {
  shouldForwardProp: (prop) => prop !== 'open',
})<AppBarProps>(({ theme, open }) => ({
  transition: theme.transitions.create(['margin', 'width'], {
    easing: theme.transitions.easing.sharp,
    duration: theme.transitions.duration.leavingScreen,
  }),
  ...(open && {
    width: `calc(100% - ${drawerWidth}px)`,
    marginLeft: `${drawerWidth}px`,
    transition: theme.transitions.create(['margin', 'width'], {
      easing: theme.transitions.easing.easeOut,
      duration: theme.transitions.duration.enteringScreen,
    }),
  }),
}));


export default function ButtonAppBar() {
  const theme = useTheme();
  const dispatch = useDispatch();
  const paletteMode = theme.palette.mode;

  const open = useSelector((state: any) => state.drawer_reducer.open);

  let logo;
  paletteMode === "dark" ? (
    logo = DarkLogo
  ) : (
    logo = LightLogo
  )

  return (
    <AppBar
      position="fixed"
      color="inherit"
      sx={{
        justifyContent: "space-between",
        padding: "1 2em",
        width: "100%",
        height: "3em",
        marginBotton: "4em",
      }}

      open={open}>
      <Toolbar>
        <IconButton
          color="inherit"
          aria-label="open drawer"
          onClick={() => dispatch(setDrawer(true))}
          edge="start"
          sx={{ mr: 2, ...(open && { display: 'none' }) }}
        >
          <MenuIcon />
        </IconButton>
        <Box
          display="flex"
          sx={{
            flexGrow: 1,
            justifyContent: "center"
          }}>
          <Box
            display="flex"
            tabIndex={0}
            aria-label='Quantum Solver Logo'
            component="img"
            sx={{
              height: '2.5rem',
              [theme.breakpoints.down("sm")]: {
                height: '2rem',
              }
            }}

            alt="Quantum Solver Logo"
            src={logo}
          />
          <Typography
            tabIndex={0}
            variant='h2'
            component="h1"
            sx={{ fontFamily: '"Helvetica Neue"', fontWeight: "regular", marginLeft: "10px", margin: "left" }} >
            QUANTUM SOLVER
          </Typography>
        </Box>

        <Box
          display="flex"
          sx={{ justifyItems: "right", marginRight: "1em" }}
        >
          <IconButton
            tabIndex={0}
            aria-label='Button to switch dark and light theme'
            onClick={() => {
              if (theme.palette.mode === "dark") {
                dispatch(set_theme_light_action());
              } else {
                dispatch(set_theme_dark_action());
              }
            }}>
            {paletteMode === "dark" ? (
              <DarkModeOutlinedICon />
            ) : (
              <LightModeOutlinedIcon />
            )}
          </IconButton>
        </Box>
      </Toolbar>
    </AppBar>
  );
}
