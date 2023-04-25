import { THEME_DARK, THEME_LIGHT } from "../actions/typeActions";
import { themeSettings } from "./ThemeFunctions/CustomTheme";
import { createTheme } from '@mui/material/styles';

// Set defult vaule of the theme
export const default_theme_mode = {
	mode: "dark",
	Theme: createTheme(themeSettings("dark"))
};

const theme_mode_reducer = (state = default_theme_mode, action: { type: string, mode: string }) => {
	switch (action.type) {
		case THEME_LIGHT: {
			return {
				...state,
				mode: action.mode,
				Theme: createTheme(themeSettings(action.mode), [action.mode])
			}
		}
		case THEME_DARK: {
			return {
				...state,
				theme: action.mode,
				Theme: createTheme(themeSettings(action.mode), [action.mode])
			}
		}
		default:
			return state;
	}
};

export default theme_mode_reducer;