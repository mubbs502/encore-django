import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import ForgotView from '../views/ForgotView.vue'
import PlaylistsView from '../views/PlaylistsView.vue'
import CreateView from '../views/CreateView.vue'
import ProfileView from '../views/ProfileView.vue'
import PlaylistView from '../views/PlaylistView.vue'
import { useUserStore } from '../stores/user.js'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
      meta: {
        disableIfLoggedIn: true,
      }
    },
    {
      path: '/forgot',
      name: 'forgot',
      component: ForgotView,
      meta: {
        disableIfLoggedIn: true,
      }
    },
    {
      path: '/playlists',
      name: 'playlists',
      component: PlaylistsView,
      meta: {
        requiresAuth: true
      }
    },
    {
      path: '/create',
      name: 'create',
      component: CreateView,
      meta: {
        requiresAuth: true
      }
    },
    // {
    //   path: '/about',
    //   name: 'about',
    //   // route level code-splitting
    //   // this generates a separate chunk (About.[hash].js) for this route
    //   // which is lazy-loaded when the route is visited.
    //   component: () => import('../views/AboutView.vue')
    // },
    {
      path: '/profile/:name',
      name: 'profile',
      component: ProfileView,
      meta: {
        requiresAuth: false
      }
    },
    {
      path: '/playlists/:name',
      name: 'playlist',
      component: PlaylistView,
      meta: {
        requiresAuth: false
      }
    },
  ]
})
router.beforeEach((to, from, next) => {
  const userStore = useUserStore()
  if (to.meta.disableIfLoggedIn) {
    // console.log(userStore.user.isAuthenticated)
    if (userStore.user.isAuthenticated) {
      next({
        name: 'playlists'
      })
      
    } else {
      next()
    }
  } 
  else if (to.meta.requiresAuth) {
  
    if (userStore.user.isAuthenticated) {
      next()
    } else {
      next({
        name: 'home'
      })
    }
  } else {
    next()
  }

})
export default router
