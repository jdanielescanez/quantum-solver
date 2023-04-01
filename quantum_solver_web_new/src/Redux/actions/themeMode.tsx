import {THEME_LIGHT, THEME_DARK} from './typeActions';


export const set_theme_light_action = () => {
    return {
        type: THEME_LIGHT,
        mode: "light"
    }
}

export const set_theme_dark_action = () => {
    return {
        type: THEME_DARK,
        mode: "dark"
    }
}