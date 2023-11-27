<template>
<div :style="{'width': width, 'height': height}">
    <button class="button-cart" :style="{'font-size': font}"  @click="addProductsInShoppingCart">ADD TO CART</button>
    
    <span class="message">{{ message }}</span>
</div>
</template>

<script>
import { useStore } from '../stores/store';

export default{
    props:{
        products:{
            type: Object,

        },
        width:{
            type: String,
            default: '50%'
        },
        height:{
            type: String,
            default: '50px'
        },
        font:{
            type: String,
            default: '16px'
        }
    },
    data(){
        return{
            message: '',
        }
    },
    
    methods:{
        addProductsInShoppingCart(){
            const store = useStore()
            if(this.products){
                const productExistInList = store.listShoppingCart.some(item => item.id === this.products.id)

                if (productExistInList){
                    store.deleteItemFromShoppingCart(this.products.id)
                    this.message = 'Produto retirado do carrinho';
                    setTimeout(() => {
                        this.message = '';
                    }, 2000)
                } else{
                    store.addToShoppingCart(this.products)
                    this.message = 'Produto adicionado ao carrinho';
                    setTimeout(() => {
                        this.message = '';
                    }, 2000)
                }
                
            }
            
            
        }
    }
}
</script>

<style scoped>

.button-cart{
    border: none;
    background-color: #171416;
    color: white;
    border-radius: 7px;
    cursor: pointer;
    width: 100%;
    height: 100%;
    margin-bottom: 10px;
}
.button-cart:hover{
    background-color: #0e0c0e;
    
}
.message{
    color: #373536;
}
</style>