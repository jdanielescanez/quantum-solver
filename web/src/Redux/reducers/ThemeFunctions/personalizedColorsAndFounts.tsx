//imports functions
import { colorTokens } from './colorsTokensPallete';


export const themeFormat = (mode: string, theme:any): any => {

  // font family.
  const titleFontFamily = 'Source Sans Pro';
  const buttonFontFamily = 'Source Sans Pro';
  const alertsFontFamily = 'Source Sans Pro';
  const textFontFamily = 'Helvetica';

  // fount VARIANT
  const titleh1 = "h3";
  const titleh2 = "h3";
  const titleh3 = "h4";
  const titleh4 = "h5";
  const titleh5 = "h6";
  const titleh6 = "h6";

  const textButton = "subtitle1";
  const textSize = "h6";

  const listDrawerFontSize = "20px";

  // alert variant filled
  const alertVariant = "filled"

  //  links decoration
  const linksDecoration = "underline";

  // font weight
  const fontWeightTitles = "bold";
  const fontWeightButton = "bold";
  const fontWeightAlerts = "bold";
  const fontWeightText = "regular";
  const linkFontWeight = "italic";


  // colors elements
  const colorButton = colorTokens(theme.palette.mode).blueAccent[500];
  const colorLinks = colorTokens(theme.palette.mode).grey[100];
  const colorTarjeta = colorTokens(theme.palette.mode).grey[800];
  const colorTrajetaLight = colorTokens(theme.palette.mode).grey[900];
  const color = colorTokens(theme.palette.mode).primary[100];

  // color font alerts (Accesibility contrast)
  const success = "white"
  const error = "white"
  const warning = "black" 


  switch (mode) {
    // font family
    case "titleFontFamily":
      return titleFontFamily;
    case "textFontFamily":
      return textFontFamily;
    case "buttonFontFamily":
      return buttonFontFamily;
    case "alertsFontFamily":
      return alertsFontFamily;

    // font weight
    case "titleFontWeight":
      return fontWeightTitles;
    case "textFontWeight":
      return fontWeightText;
    case "buttonFontWeight":
      return fontWeightButton;
    case "alertsFontWeight":
      return fontWeightAlerts;
    case "linkFontWeight":
      return linkFontWeight;

    // font VARIANT
    case "titleh1":
      return titleh1;
    case "titleh2":
      return titleh2;
    case "titleh3":
      return titleh3;
    case "titleh4":
      return titleh4;
    case "titleh5":
      return titleh5;
    case "titleh6":
      return titleh6;


    case "textButton":
      return textButton;
    case "textSize":
      return textSize;

    case "listDrawerFontSize":
      return listDrawerFontSize;
    
    // alert variant filled
    case "alertVariant":
      return alertVariant;
    
    //  links decoration
    case "linksDecoration":
      return linksDecoration;

    //colors elements
    case "colorButton":
      return colorButton;
    case "colorLinks":
      return colorLinks;
    case "colorTarjeta":
      return colorTarjeta;
    case "colorTrajetaLight":
      return colorTrajetaLight;
    case "color":
      return color;

    // color font alerts 
    case "success":
      return success;
    case "error":
      return error;
    case "warning":
      return warning;

    default:
      return "";
  }

}