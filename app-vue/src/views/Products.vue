<template>
    <section>
        <div class="category-title">
            <h2>{{ nameCurrentCategory }}</h2>
        </div>
        <div class="buttons">
            <button class="filter-button">FILTERS</button>
            <button class="sort-button">SORT BY +</button>
        </div>

        <ProductCard :products="products">
        
        </ProductCard>

    </section>
    
</template>

<script>
import { useStore } from '../stores/store';
import axios from 'axios';
import ProductCard from '../components/ProductCard.vue';

export default{
    data(){
        return{
            products: null
        }
    },
    components:{
        ProductCard,
    },
    mounted(){
        const idCurrentCategory = useStore().idCurrentCategory
        this.fetchDataProducts(idCurrentCategory)
    },
    watch:{
        idCurrentCategory(newCategory, oldCategory){
            if(newCategory !== oldCategory){
                this.fetchDataProducts(newCategory)
            }
        }
    },
    methods:{
        fetchDataProducts(idCategory){
            axios.get(`http://127.0.0.1:8000/api/products/category/${idCategory}`)
            .then(response => {
                this.products = response.data
            })
            .catch(error => {
                console.log('Erro ao buscar os dados', error)
            })
        }
        
    },
    computed:{
        nameCurrentCategory(){
            return useStore().currentCategory
        },
        idCurrentCategory(){
            return useStore().idCurrentCategory
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
</style>