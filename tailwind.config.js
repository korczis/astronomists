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
