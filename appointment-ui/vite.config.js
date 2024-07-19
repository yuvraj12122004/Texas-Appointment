import { fileURLToPath, URL } from 'node:url'
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

import { createRequire } from 'node:module';
const require = createRequire( import.meta.url );
//const path = import.meta.env.VITE_DEPLOYMENT_PATH;

// https://vitejs.dev/config/
export default defineConfig({
  mode: 'development',
  base: '/Scheduler',
  plugins: [
    vue(),
    //ckeditor5( { theme: require.resolve( '@ckeditor/ckeditor5-theme-lark' ) } )
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  },
  build: {
    chunkSizeWarningLimit: 1600,
  //   rollupOptions: {
  //     output:{
  //         manualChunks(id) {
  //             if (id.includes('node_modules')) {
  //               console.log(id);
  //                 return id.toString().split('node_modules/')[1].split('/')[0].toString();
  //             }
        
  //         }
  //   
  // }
  }
})
