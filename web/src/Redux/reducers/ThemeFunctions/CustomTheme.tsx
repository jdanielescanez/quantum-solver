import React from 'react';
import { createTheme } from '@mui/material/styles';
import { responsiveFontSizes } from '@mui/material/styles';
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
		typography: {
			fontFamily: [
				'Source Sans Pro',
				'Helvetica',
			].join(","),
			h1: {
				fontFamily: [
					'Source Sans Pro',
					'Helvetica',
				].join(","),
			},
			h2: {
				fontFamily: [
					'Source Sans Pro',
					'Helvetica',
				].join(","),
			},
			h3: {
				fontFamily: [
					'Source Sans Pro',
					'Helvetica',
				].join(","),
			},
			h4: {
				fontFamily: [
					'Source Sans Pro',
					'Helvetica',
				].join(","),
			},
			h5: {
				fontFamily: [
					'Source Sans Pro',
					'Helvetica',
				].join(","),
			},
			h6: {
				fontFamily: [
					'Source Sans Pro',
					'Helvetica',
				].join(","),
			},
			subtitle1: {
				fontFamily: [
					'Source Sans Pro',
					'Helvetica',
				].join(","),
			},
			subtitle2: {
				fontFamily: [
					'Source Sans Pro',
					'Helvetica',
				].join(","),
			},
			body1: {
				fontFamily: [
					'Source Sans Pro',
					'Helvetica',
				].join(","),
			},
			body2: {
				fontFamily: [
					'Source Sans Pro',
					'Helvetica',
				].join(","),
			},
		},
	};
};


// context for color mode
export const ColorModeContext = React.createContext({ toggleColorMode: () => { } });

export const useMode = () => {
	const [mode, setmode] = React.useState("dark");

	const colorMode = React.useMemo(
		() => ({
			toggleColorMode: () => {
				setmode((prevMode) => (prevMode === "light" ? "dark" : "light"));
			}
		}),
		[]
	);

	const theme:any = React.useMemo(() => responsiveFontSizes(createTheme(themeSettings(mode))), [mode]);
	
	return [theme, colorMode];
};