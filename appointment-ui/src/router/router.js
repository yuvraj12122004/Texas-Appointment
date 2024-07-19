import { createRouter, createWebHistory } from 'vue-router'


import LapdChat from '../../src/LapdChat.vue';



const routes =[ 

  // {
  //   path: '/signin',
  //   name: 'signin',
  // 	component :SignIn,
  // },
  
  {
    path: '/LAPD/LapdChat',
    name: 'LapdChat',
    component: LapdChat,
  },
  
  
]
const router = createRouter({

  history:createWebHistory(),
  routes
})
export default router