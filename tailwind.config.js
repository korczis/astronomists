/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',
    './content/**/*.md',
    './node_modules/flowbite/**/*.js',
  ],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        void: '#0a0a0a',
        presence: '#f8f8f8',
        signal: '#e63946',
        gold: '#d4a574',
        'space-blue': '#1d3557',
        growth: '#06a77d',
        'deep-gray': '#1a1a1a',
        'mid-gray': '#404040',
        'light-gray': '#e8e8e8',
        // Flowbite Pro `primary` role, mapped onto the Prague Gold accent (500 = gold).
        primary: {
          50: '#fbf6f0',
          100: '#f6ecdf',
          200: '#eed8bf',
          300: '#e4c19c',
          400: '#dcb388',
          500: '#d4a574',
          600: '#c08a52',
          700: '#a06d3d',
          800: '#7f5633',
          900: '#67462b',
        },
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', '-apple-system', 'sans-serif'],
        serif: ['Georgia', 'serif'],
        mono: ['"JetBrains Mono"', 'ui-monospace', 'SFMono-Regular', 'monospace'],
      },
      maxWidth: {
        content: '1200px',
      },
      backgroundImage: {
        'cosmic': 'radial-gradient(900px 480px at 78% -8%, rgba(29,53,87,.55), transparent 60%), radial-gradient(620px 360px at 8% 108%, rgba(212,165,116,.16), transparent 60%)',
      },
    },
  },
  plugins: [
    require('flowbite/plugin'),
    require('@tailwindcss/typography'),
  ],
};
