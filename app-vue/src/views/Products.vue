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

        <div class="pagination">
            <vue-awesome-paginate v-model="currentPage" :total-items="amountProducts"
            :items-per-page="24" :show-breakpoint-buttons="false" paginate-buttons-class="btn"
            active-page-class="btn-active"
            back-button-class="back-btn"
            next-button-class="next-btn"/>
        </div>


    </section>
    
</template>

<script>
import { useStore } from '../stores/store';
import axios from 'axios';
import ProductCard from '../components/ProductCard.vue';


export default{
    data(){
        return{
            products: null,
            currentPage: 1,
            amountProducts: null
        }
    },
    components:{
        ProductCard,      
    },
    mounted(){
        const idCurrentCategory = useStore().idCurrentCategory
        this.fetchDataProducts(idCurrentCategory, this.currentPage)
    },
    watch:{
        idCurrentCategory(newCategory, oldCategory){
            if(newCategory !== oldCategory){
                this.currentPage = 1
                this.fetchDataProducts(newCategory, this.currentPage)
            }
        },
        currentPage(newPage, oldPage){
            if(newPage !== oldPage){
                this.fetchDataProducts(this.idCurrentCategory, newPage)
            }
        }
    },
    methods:{
        fetchDataProducts(idCategory, page){
            axios.get(`http://127.0.0.1:8000/api/products/category/${idCategory}/?page=${page}`)
            .then(response => {
                this.products = response.data.results
                this.amountProducts = response.data.count
            })
            .catch(error => {
                console.log('Erro ao buscar os dados', error)
            })
        },
        
    },
    computed:{
        nameCurrentCategory(){
            return useStore().currentCategory
        },
        idCurrentCategory(){
            return useStore().idCurrentCategory
        },
        
          
    }
}
</script>

<style >
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


.pagination{
    display: flex;
    justify-content: center;
    margin-block: 10vh;
}
.pagination-container {
    display: flex;
    column-gap: 10px;
  }
  .btn {
    height: 40px;
    width: 40px;
    border-radius: 20px;
    cursor: pointer;
    background-color: rgb(242, 242, 242);
    border: 1px solid rgb(217, 217, 217);
    color: black;
  }
  .btn:hover{
    background-color: #d4cdd4;
  }
  .btn-active{
    background-color: #908d90;
    color: white;
  }
  .back-btn, .next-btn{
    background-color: #171416;
    color: white;
  }
  .back-btn:hover, .next-btn:hover{
    background-color: #171416;
  }
  
  
</style>