import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path:'/products',
      name:'products',
      component: () => import('../views/Products.vue')
    },
    {
      path:'/product-details/:id',
      name: 'productDetails',
      component: () => import('../views/ProductDetails.vue')
    },
    {
      path:'/favorite',
      name:'favorite',
      component: () => import('../views/FavoriteProducts.vue')
    },
    {
      path:'/my-cart',
      name: 'myCart',
      component: () => import('../views/ShoppingCart.vue')
    },
    {
      path:'/login',
      name: 'login',
      component: () => import('../views/Login.vue')
    },
    {
      path:'/register',
      name: 'register',
      component: () => import('../views/Register.vue')
    }
    
  ]
})

export default router
