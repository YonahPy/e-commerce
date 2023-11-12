<template>
    <section>
        <div class="category-title">
            <h2>{{ currentCategory }}</h2>
        </div>
        <div class="buttons">
            <button class="filter-button">FILTERS</button>
            <button class="sort-button">SORT BY +</button>
        </div>
        
        <div class="products">
            <div class="cart-products" v-for="product in filterProducts" :key="product.id">
               <div class="cart-image">
                <img :src="product.alternative_image" :alt="product.product_title" v-if="product.alternative_image">
                <img :src="product.image" :alt="product.product_title" v-else>
               </div>
               <div class="cart-info">
                <p>{{ product.product_title }}</p>
                <p>R$ {{ product.price }}</p>
                </div>
            
            </div>
        </div>


    </section>
    
</template>

<script>
import { useStore } from '../stores/store';
import axios from 'axios';

export default{
    data(){
        return{
            products: null
        }
    },
    mounted(){
        this.fetchDataProducts()
    },
    methods:{
        fetchDataProducts(){
            axios.get('http://127.0.0.1:8000/api/products/')
            .then(response => {
                this.products = response.data
            })
            .catch(error => {
                console.log('Erro ao buscar os dados', error)
            })
        }
        
    },
    computed:{
        currentCategory(){
            return useStore().currentCategory
        },
        idCurrentCategory(){
            return useStore().idCurrentCategory
        },
        filterProducts(){
            if (this.products){
                return this.products.filter(product => {
                    return product.category === this.idCurrentCategory
                })
            }
        }
        
    }
}
</script>

<style scoped>
.category-title{
    margin-left: 4vw;
    margin-block: 30px;
}
.category-title h2{
    font-family: 'Manrope', sans-serif;
    font-size: 60px;
}
.buttons{
    margin-inline: 4vw;
    display: flex;
    justify-content: space-between;
    margin-bottom: 6vh;
}
.buttons button{
    border-radius: 5px;
    width: 120px;
    height: 40px;
    cursor: pointer;
    font-size: 16px;
    letter-spacing: 2px;
}
.filter-button{
    border: none;
    background-color: #171416;
    color: white;
    
}
.filter-button:hover{
    background-color: white;
    border: 2px solid #171416;
    color: #171416;
}
.sort-button{
    border: 2px solid #373536;
    background-color: transparent;
    color: #373536;
}
.sort-button:hover{
    background-color: #373536;
    color: white;
}
.products{
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    margin-inline: 4vw;
    gap: 20px;
    
}

.cart-image img{
    width: 100%;
    margin-bottom: 10px;
}

.cart-info p{
    margin-top: 5px;
}
</style>