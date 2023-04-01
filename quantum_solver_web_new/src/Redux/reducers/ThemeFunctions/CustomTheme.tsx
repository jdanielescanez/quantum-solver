import { colorTokens } from './colorsTokensPallete'


export const themeSettings = (mode: any) => {
    const colors = colorTokens(mode);

    return {
        palette: {
            mode: mode,
            ...(mode === "dark"
                ? {
                    // palette values for dark mode
                    primary: {
                        main: colors.primary[500],
                    },
                    secondary: {
                        main: colors.greenAccent[500],
                    },
                    neutral: {
                        dark: colors.grey[700],
                        main: colors.grey[500],
                        light: colors.grey[100],
                    },
                    background: {
                        default: colors.primary[500],
                    },
                }
                : {
                    // palette values for light mode
                    primary: {
                        main: colors.primary[100],
                    },
                    secondary: {
                        main: colors.greenAccent[500],
                    },
                    neutral: {
                        dark: colors.grey[700],
                        main: colors.grey[500],
                        light: colors.grey[100],
                    },
                    background: {
                        default: "#fcfcfc",
                    },
                }),
        },
        breakpoints: {
            values: {
                xs: 0,
                sm: 600,
                md: 900,
                lg: 1200,
                xl: 1600,
            },
        },
        typography: {
            fontFamily: ["Source Sans Pro", "sans-serif", '"Helvetica Neue"'].join(","),
            fontSize: 20,
            h1: {
                fontFamily: ["Source Sans Pro", "sans-serif", '"Helvetica Neue"'].join(","),
                fontSize: 40,
            },
            h2: {
                fontFamily: ["Source Sans Pro", "sans-serif", '"Helvetica Neue"'].join(","),
                fontSize: 32,
            },
            h3: {
                fontFamily: ["Source Sans Pro", "sans-serif", '"Helvetica Neue"'].join(","),
                fontSize: 30,
            },
            h4: {
                fontFamily: ["Source Sans Pro", "sans-serif", '"Helvetica Neue"'].join(","),
                fontSize: 28,
            },
            h5: {
                fontFamily: ["Source Sans Pro", "sans-serif", '"Helvetica Neue"'].join(","),
                fontSize: 25,
            },
            h6: {
                fontFamily: ["Source Sans Pro", "sans-serif", '"Helvetica Neue"'].join(","),
                fontSize: 20,
            },
        },
    };
};