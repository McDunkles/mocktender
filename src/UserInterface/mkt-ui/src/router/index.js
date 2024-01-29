import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: '/',
      component: HomeView
    },
    {
      path: '/machineSelect',
      name: '/machineSelect',
      component: () => import('../views/MachineSelectView.vue')
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('../views/LoginView.vue')
    },
    {
      path: '/menu',
      name: 'menu',
      component: () => import('../views/MainMenuView.vue')
    },
    {
      path: '/make',
      name: 'make',
      component: () => import('../views/MakeDrinkView.vue')
    },
    {
      path: '/make/addRecipe',
      name: 'make/addRecipe',
      component: () => import('../views/AddRecipeView.vue')
    },
    {
      path: '/viewLiquidLevels',
      name: 'viewLiquidLevels',
      component: () => import('../views/LiquidLevelsView.vue')
    },
    {
      path: '/settings',
      name: 'settings',
      component: () => import('../views/SettingsView.vue')
    },
    {
      path: '/adminSettings',
      name: 'adminSettings',
      component: () => import('../views/AdminSettingsView.vue')
    }
  ]
})

export default router
