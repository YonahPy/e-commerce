import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import { useStore } from '../stores/store'

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
    },
    {
      path: '/search/:search',
      name: 'search',
      component: () => import('../views/SearchView.vue')
    },
    {
      path: '/checkout',
      name: 'checkout',
      component: () => import('../views/Checkout.vue')
    },
    {
      path:'/successful-payment',
      name: 'successPayment',
      component: () => import('../views/SuccessPayment.vue'),
      meta: {requiresPayment: true},

    },
    {
      path:'/:pathMatch(.*)*',
      name: 'NotFound',
      component: () => import('../views/NotFound.vue')
    }
    
  ]
})

router.beforeEach((to, from, next) => {
  const requiresPayment = to.matched.some(record => record.meta.requiresPayment)
  const isPaymentComplete = useStore().isPaymentComplete
  const isCheckoutAllowed = useStore().isCheckoutAllowed;

  if (to.path === '/checkout'){
    if(isCheckoutAllowed){
      next()
    } else{
      next('/:pathMatch(.*)*')
    }
  } else if (requiresPayment){
    if(isPaymentComplete){
      next();
    }else{
      next('/:pathMatch(.*)*');
    }
  } else{
    next();
  } 
  
 
   
});

export default router
