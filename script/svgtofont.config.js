const path = require("path");

module.exports = {
  fontName: "gaiasky-icons", // Font name
  css: true, // Generate a CSS file
  classNamePrefix: "gs", // Prefix for CSS class names
  website: {
    title: "Gaia Sky Icons",
    favicon: "../static/img/icon.png",
    logo: "../static/img/brand/gs_icon.svg",
    version: "1.0.0",
    meta: {
      description: "Gaia Sky icon font",
      keywords: "icons, font, svg"
    }
  }
};
