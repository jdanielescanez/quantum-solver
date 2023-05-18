import Box from '@mui/material/Box'
import Image from "../assets/Banner.png"
import { useTheme } from '@mui/material';

export default function Banner() {
  const theme = useTheme();
  return (
    <Box
      tabIndex={0}
      aria-label='Banner of the page'
      sx={{
        backgroundImage: `linear-gradient(rgba(0, 0, 0, 0), rgba(0, 0, 0, 0)), url(${Image})`,
        width: "100%",
        height: "75vh",
        backgroundPosition: "center",
        backgroundRepeat: "no-repeat",
        backgroundSize: "100% 100%",     
      }}>
    </Box>
  );
}
