import Box from '@mui/material/Box'
import Image from "../assets/Img1.png"
import { useTheme } from '@mui/material';

export default function Banner() {
    const theme = useTheme();
    return (
        <Box
            tabIndex={0}
            aria-label='Banner of the page'
            sx={{
                marginY: "0",
                backgroundImage: `linear-gradient(rgba(0, 0, 0, 0), rgba(0, 0, 0, 0)), url(${Image})`,
                width: "100%",
                height: "700px",
                backgroundPosition: "center",
                backgroundRepeat: "no-repeat",
                backgroundSize: "cover",
                position: "relative",
                display: "flex",
                justifyContent: "center",
                [theme.breakpoints.down("sm")]: {
                    height: "300px",
                },
                [theme.breakpoints.between("sm","md")]: {
                    height: "400px",
                },
                [theme.breakpoints.between("md","lg")]: {
                    height: "500px",
                },
                [theme.breakpoints.between("lg","xl")]: {
                    height: "600px",
                },
                [theme.breakpoints.up("xl")]: {
                    height: "1000px",
                }
            }}>
        </Box>
    );
}
