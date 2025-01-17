import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
  // Basis-URL für die Bereitstellung auf Vercel
  base: '/',

  plugins: [react()],

  build: {
    outDir: 'dist', // Der Output-Ordner für den Build
  },
})
