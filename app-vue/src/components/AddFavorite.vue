<template>
    <button class="button-favorite" @click="addProductsInFavoriteList" :class="{'isActive': isActive, 'circle': circle}">
        <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" width="256" height="256" viewBox="0 0 256 256" xml:space="preserve">
        <defs>
        </defs>
        <g style="stroke: none; stroke-width: 0; stroke-dasharray: none; stroke-linecap: butt; stroke-linejoin: miter; stroke-miterlimit: 10; fill: none; fill-rule: nonzero; opacity: 1;" transform="translate(1.4065934065934016 1.4065934065934016) scale(2.81 2.81)" >
            <path d="M 84.646 11.504 C 75.554 1.233 58.335 -0.041 45 13.074 C 31.665 -0.041 14.446 1.233 5.354 11.504 c -9.671 10.926 -5.609 31.318 7.123 47.615 C 18.931 67.38 34.874 80.832 45 86.481 c 10.126 -5.649 26.069 -19.101 32.523 -27.362 C 90.255 42.822 94.318 22.43 84.646 11.504 z" style="stroke: none; stroke-width: 1; stroke-dasharray: none; stroke-linecap: butt; stroke-linejoin: miter; stroke-miterlimit: 10; fill: rgb(248,48,95); fill-rule: nonzero; opacity: 1;" transform=" matrix(1 0 0 1 0 0) " stroke-linecap="round" />
        </g>
        </svg>
    </button>

    
</template>

<script>
import {useStore} from '../stores/store'
export default{
    data(){
        return{
            isActive: false,
        }
    },
    props:['products', 'circle'],
    mounted(){
        this.store = useStore()
        this.productExistInList()
    },
    methods:{
        addProductsInFavoriteList(){     
            this.isActive = !this.isActive
            const store = useStore()  
            

            if (this.isActive && this.products ){
               store.listFavoriteProducts.push(this.products)
               
            } else if(!this.isActive){
                this.store.deleteItemFromFavoriteList(this.products.id);
                
            }
        },
        productExistInList(){
            const store = useStore();
            if (this.products){
                const existInFavorites = store.listFavoriteProducts.some(item => item.id === this.products.id)

                if(existInFavorites){
                    this.isActive = true
                }
            }          
        }     
    }
}
</script>

<style scoped>

.button-favorite{
    height: 50px;
    border-radius: 7px;
    cursor: pointer;
    width: 15%;
    border: 1px solid #171416;
    margin-left: 15px;
    display: flex;
    align-items: center;
    justify-content: center;
    background-color: transparent;
}
.circle{
    width: 10%;
    height: 40px;
    border-radius: 50%;
    border: none;
    align-items: end;
    
}
.button-favorite svg{
    width: 100%;
   height: 60%;
   
}
.button-favorite  svg path{
    fill: white !important;
    stroke: #0e0c0e !important;
    stroke-width: 3 !important;
}
.button-favorite:hover  svg path{
    fill: rgb(248,48,95) !important;
    stroke: rgb(248,48,95) !important;
    
}
.isActive  svg path{
    fill: rgb(248,48,95) !important;
    stroke: rgb(248,48,95) !important;
}

</style>