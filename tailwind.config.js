/*
 ** Docs: https://tailwindcss.com/docs/configuration
 ** Default: https://github.com/tailwindcss/tailwindcss/blob/master/stubs/defaultConfig.stub.js
 */

module.exports = {
  future: {
    removeDeprecatedGapUtilities: true,
    purgeLayersByDefault: true,
  },
  experimental: {
    applyComplexClasses: true,
  },
  purge: {
    // enabled: true,
    content: ['./**/*.html'],
  },
  theme: {
    container: {
      center: true,
    },
    extend: {
      screens: {
        '2xl': '1536px',
      },
    },
    variants: {},
    plugins: [],
  },
};
