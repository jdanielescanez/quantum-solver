import {
  Routes,
  Route
} from 'react-router-dom'
import { useSelector } from 'react-redux';

// MUI imports
import { styled } from '@mui/material/styles';

//components imports
import Navbar from './components/navBar';
import DrawerContent from './components/drawer';
import Footer from './components/footer';

// Pages imports
import { Welcome } from './pages/welcome';
import { Login } from './pages/login';
import { AlgorithmsInformation } from './pages/algorithmsInformation'
import { RunAlgorithms } from './pages/runAlgorithms';



const drawerWidth = 240;


const Main = styled('main', { shouldForwardProp: (prop) => prop !== 'open' })<{
  open?: boolean;
}>(({ theme, open }) => ({
  flexGrow: 1,
  transition: theme.transitions.create('margin', {
    easing: theme.transitions.easing.sharp,
    duration: theme.transitions.duration.leavingScreen,
  }),
  marginLeft: `-${drawerWidth}px`,
  ...(open && {
    transition: theme.transitions.create('margin', {
      easing: theme.transitions.easing.easeOut,
      duration: theme.transitions.duration.enteringScreen,
    }),
    marginLeft: 0,
  }),
}));


const DrawerHeader = styled('div')(({ theme }) => ({
  display: 'flex',
  alignItems: 'center',
  padding: theme.spacing(0, 1),
  // necessary for content to be below app bar
  ...theme.mixins.toolbar,
  justifyContent: 'flex-end',
}));



const PrincipalContainer = () => {
  const open = useSelector((state: any) => state.drawer_reducer.open);
  console.log(open)

  return (
    <>
      <Navbar />
      <DrawerContent />

      <Main open={open}>
        <DrawerHeader />
        <Routes>
          <Route path="/" element={<Welcome />} />
          <Route path="/login" element={<Login />} />
          <Route path="/algorithms" element={<AlgorithmsInformation />} />
          <Route path="/algorithmsRun" element={<RunAlgorithms />} />
          <Route path="*" element={<Welcome />} />
        </Routes>
        <Footer />
      </Main>
    </>
  )
}

export default PrincipalContainer;