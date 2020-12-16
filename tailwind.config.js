const colors = require('tailwindcss/colors');

module.exports = {
  purge: {
    // enabled: true,
    content: ['./**/*.html'],
  },
  darkMode: false, // or 'media' or 'class'
  theme: {
    container: {
      center: true,
    },
    extend: {
      colors: {
        teal: colors.teal,
      },
      gridTemplateColumns: {
        sound: 'minmax(0, 16rem) 10fr 1fr 1fr',
        'sound-edit': 'minmax(0, 16rem) 10fr 1fr 1fr 1fr',
      },
    },
  },
  variants: {
    extend: {},
  },
  plugins: [],
};
