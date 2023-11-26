import {defineStore} from 'pinia'
import { reactive } from 'vue';

const STORAGE_KEY = 'app-vue';

export const useStore = defineStore({
    id: 'main',
    state: () => ({
        currentCategory: '',
        idCurrentCategory: null,
        listFavoriteProducts: reactive([]),
        listShoppingCart: reactive([]),
        token: '',
        
    }),
    actions:{
        setCategory(name, id){
            this.currentCategory = name;
            this.idCurrentCategory = id;
            this.persistState();
            
        },

        deleteItemFromFavoriteList(idProduct){
            const index = this.listFavoriteProducts.findIndex((product) => product.id === idProduct);

            if (index !== -1){
                this.listFavoriteProducts.splice(index, 1);
            }
        },
        addToShoppingCart(product){
            const cartProduct = { ...product, quantity: 1};
            this.listShoppingCart.push(cartProduct)
        },
        deleteItemFromShoppingCart(idProduct){
            const index = this.listShoppingCart.findIndex((product) => product.id === idProduct);

            if(index !== -1){
                this.listShoppingCart.splice(index, 1);
            }
        },
        setToken(token){
            this.token = token
        },
        persistState(){
            localStorage.setItem(STORAGE_KEY, JSON.stringify(this.$state));
        },
        restoreState(){
            const savedState = localStorage.getItem(STORAGE_KEY);
            if(savedState){
                Object.assign(this.$state, JSON.parse(savedState));
            }
        },
    },
   
});