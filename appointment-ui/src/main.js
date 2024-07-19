//bootstrap min css
//import '../node_modules/bootstrap/dist/css/bootstrap.min.css'
//import { bootstrap } from 'bootstrap';
import './assets/css/style.css'

import { createPinia } from 'pinia'
//font awesome icons
/* import the fontawesome core */
import { library } from '@fortawesome/fontawesome-svg-core'
/* import font awesome icon component */
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
/* import specific icons */
import {faAdd, faCircleXmark, faFileMedical, faCaretUp, faCaretDown, faPencil, faCircleCheck, faRotate, faCircleExclamation, faCirclePlus, faMagnifyingGlass, faArrowLeft, faEyeSlash, faEye, faArrowRightFromBracket, faBars, faFile, faCopy, faFileImport, faPaperPlane, faTrash, faToggleOn, faToggleOff, faFilePdf ,faFileWord , faFileAlt ,faFileArchive, faBolt, faFileExcel, faPlay, faPause, faStop,faRotateRight} from '@fortawesome/free-solid-svg-icons'
/* add icons to the library */
library.add(faAdd, faCircleXmark, faFileMedical, faCaretUp, faCaretDown, faPencil, faCircleCheck, faRotate, faCircleExclamation, faCirclePlus, faMagnifyingGlass, faArrowLeft, faEyeSlash, faEye, faArrowRightFromBracket, faBars, faFile, faCopy, faFileImport, faPaperPlane, faTrash,faToggleOn, faToggleOff, faFilePdf, faFileWord ,faFileAlt , faFileArchive, faBolt,faFileExcel, faPlay, faPause, faStop,faRotateRight);
import '@fortawesome/fontawesome-svg-core/styles.css'; // Ensure you import FontAwesome CSS


//bootstrap min js
//import '../node_modules/bootstrap/dist/js/bootstrap.bundle.min'
//import { Modal } from '../node_modules/bootstrap/dist/js/bootstrap.bundle.min'
// import '../node_modules/@vueform/multiselect/themes/default.css'
// import 'vue-loading-overlay/dist/css/index.css';
// import 'mosha-vue-toastify/dist/style.css';
// import  Loading  from 'vue-loading-overlay'
import { createApp } from 'vue'
import App from './App.vue'
// import router from '../src/router/router'
// import store from './stores/store';
// import '@popperjs/core';
// import { defineComponent } from "vue";
// import Popper from "vue3-popper";
// import Multiselect from '@vueform/multiselect'
// import VueApexCharts from "vue3-apexcharts";	


const app = createApp(App);
app.component('font-awesome-icon', FontAwesomeIcon)
// app.use(VueApexCharts);
// app.use(router)
// app.use(store);
//app.use(Modal);
// app.component('loading-overlay', Loading)
app.use(createPinia())
// app.component("Popper", Popper);
// app.component("Multiselect", Multiselect)
app.mount('#app')

