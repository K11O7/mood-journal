/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    '../templates/**/*.html',
    '../../journal/templates/**/*.html',
    './templates/**/*.html'
  ],
  safelist: [
    'font-dancing',
  ],
  theme: {
    extend: {
      fontFamily: {
        dancing: ['"Dancing Script"', 'cursive'],
      },
    },
  },
  plugins: [],
}
