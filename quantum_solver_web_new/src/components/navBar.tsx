// React - Redux import
import { useDispatch, useSelector } from 'react-redux';
import { useNavigate } from "react-router-dom";
import React from 'react';

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

import {
  logout
} from '../Redux/actions/LoginActions'

//icons
import LightModeOutlinedIcon from '@mui/icons-material/LightModeOutlined';
import DarkModeOutlinedICon from '@mui/icons-material/DarkModeOutlined';
import LogoutOutlinedIcon from '@mui/icons-material/LogoutOutlined';

// assets
import LightLogo from '../assets/LightLogo192.png';
import DarkLogo from '../assets/DarkLogo192.png';

// Fuctions
import { themeFormat } from '../Redux/reducers/ThemeFunctions/personalizedColorsAndFounts';
import { ColorModeContext } from '../Redux/reducers/ThemeFunctions/CustomTheme';

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
  let navigate = useNavigate();

  const colorMode = React.useContext(ColorModeContext);

  const paletteMode = theme.palette.mode;
  const open = useSelector((state: any) => state.drawer_reducer.open);

  const { token } = useSelector((state: any) => state.login_reducer)
  const { isToken } = useSelector((state: any) => state.login_reducer)

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
        height: "auto",
        marginBotton: "4em",
      }}

      open={open}>
      <Toolbar
        sx={{
          display: "flex",
        }}>
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
            justifyContent: "center",
            alignItems: "center",
            marginBotton: "1%",
          }}>
          <Box
            display="flex"
            tabIndex={0}
            aria-label='Quantum Solver Logo link to Home page'
            component="img"
            onClick={() => {
              navigate("/")
            }}
            sx={{
              height: '2rem',
              [theme.breakpoints.down("sm")]: {
                height: '1.5rem',
              }
            }}

            alt="Quantum Solver Logo"
            src={logo}
          />
          <Typography
            tabIndex={0}
            aria-label="QUANTUM SOLVER, Link to Home page"
            onClick={() => {
              navigate("/")
            }}
            variant={themeFormat("titleh3",theme)}
            component="h1"
            sx={{
              fontFamily: themeFormat("titleFontFamily",theme),
              fontWeight: themeFormat("textFontWeight",theme),
              margin: "left",
              marginLeft: "10px",
            }} 
            >
            QUANTUM SOLVER
          </Typography>
        </Box>


        <Box
          display="flex"
          sx={{
            justifyItems: "right",
          }}
        >
          <IconButton
            tabIndex={0}
            aria-label='Button to switch dark and light theme'
            onClick={colorMode.toggleColorMode}
            sx={{
              height: '4rem',
              [theme.breakpoints.down("sm")]: {
                height: '1.5rem',
              },
              [theme.breakpoints.down("xs")]: {
                height: '1rem',
              }
            }}
          >
            {paletteMode === "dark" ? (
              <DarkModeOutlinedICon
                sx={{
                  height: '2rem',
                  [theme.breakpoints.down("sm")]: {
                    height: '1.5rem',
                  }
                }}
              />
            ) : (
              <LightModeOutlinedIcon/>
            )}
          </IconButton>

          {
            isToken ?
              <Box
                display="flex"
                sx={{
                  justifyItems: "right",
                  marginLeft: "auto"
                }}
              >
                <IconButton
                  tabIndex={0}
                  aria-label='Button to Logout'
                  onClick={() => {
                    dispatch(logout(token));
                    navigate("/login")
                  }}
                  sx={{
                    height: '4rem',
                    [theme.breakpoints.down("sm")]: {
                      height: '1.5rem',
                    },
                    [theme.breakpoints.down("xs")]: {
                      height: '1rem',
                    }
                  }}
                >
                  <LogoutOutlinedIcon/>
                </IconButton>
              </Box>
              :
              null
          }
        </Box>
      </Toolbar>
    </AppBar >
  );
}
