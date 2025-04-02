import { createRouter, createWebHistory } from 'vue-router'
import axios from 'axios';
import { endpoints } from '/common/endpoints';
import HelloWorld from '@/components/HelloWorld.vue';
import Login from '@/components/Login.vue';
import Registration from '@/components/Registration.vue';
import PageBeforeLogin from '../components/PageBeforeLogin.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'Start',
      component: HelloWorld
    },
    { path: '/login',
      name: 'Login',
      component: Login,
      beforeEnter: async (to, from, next) => {
        try {
          const response = await axios.get(`${endpoints.check_auth}`, { withCredentials: true });
          if (response.data.authenticated) {
            next("/dashboard");
          } else {
            next();
          }
        } catch (error) {
          next();
        }
      },
    },
    { path: '/registration',
      name: 'Registration',
      component: Registration,
      beforeEnter: async (to, from, next) => {
        try {
          const response = await axios.get(`${endpoints.check_auth}`, { withCredentials: true });
          if (response.data.authenticated) {
            next("/dashboard");
          } else {
            next();
          }
        } catch (error) {
          next();
        }
      },
    },
    {
      name: 'dashboard',
      path: "/dashboard",
      component: PageBeforeLogin,
      beforeEnter: async (to, from, next) => {
        try {
          const response = await axios.get(`${endpoints.check_auth}`, { withCredentials: true });
          if (response.data.authenticated) {
            next();
          } else {
            next("/login");
          }
        } catch (error) {
          next("/login");
        }
      },
    },
  ],
})

export default router
