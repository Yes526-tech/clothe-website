/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        burgundy: {
          500: '#7A1F3D',
          700: '#5A122A',
          900: '#3A0B1A',
        },
        emerald: {
          700: '#0F4C3A',
          900: '#0A3326',
        },
        gold: {
          400: '#F2D27A',
          500: '#D4AF37', // Brand Accent
          600: '#AA8C2C',
        },
        parchment: {
          100: '#FDF5E6',
          200: '#F5E6D3',
          300: '#E8D5B5',
        }
      },
      fontFamily: {
        serif: ['"Playfair Display"', 'serif'],
        sans: ['"Inter"', 'sans-serif'],
      },
      backgroundImage: {
        'parchment-texture': "url('/textures/parchment.png')",
      }
    },
  },
  plugins: [],
}
