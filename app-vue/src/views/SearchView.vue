<template>
    <section>
        <div class="current-search">
            <h2>Search: {{ searchUrl }}({{ amountProducts }})</h2>
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
import axios from 'axios';
import ProductCard from '../components/ProductCard.vue';

export default{
    data(){
        return{
            products: null,
            currentPage: 1,
            amountProducts: null,
            search: '',
        }
    },
    components:{
        ProductCard,      
    },
    mounted(){
        const searchText = this.$route.params.search;
        this.search = searchText;
        this.fetchSearchedProducts(this.search, this.currentPage)
    },
    watch:{
        currentPage(newPage, oldPage){
            if(newPage !== oldPage){
                this.fetchSearchedProducts(this.search, newPage)
            }
        },
        searchUrl(newSearch, oldSearch){
            if(newSearch !== oldSearch){
                this.currentPage = 1
                this.fetchSearchedProducts(newSearch, this.currentPage)
            }
        }
    },
    computed:{
        searchUrl(){
            return this.$route.params.search
        }
    },
    methods:{
        fetchSearchedProducts(search, page){
            axios.get(`http://127.0.0.1:8000/api/products/search/${search}/?page=${page}`)
            .then(response => {
                this.products = response.data.results
                this.amountProducts = response.data.count
            })
            .catch(error => {
                console.log('Erro ao buscar os dados', error)
            })
        },
        
    },
}
</script>

<style>

.current-search{
    margin-left: 4vw;
    margin-block: 30px;
}
.current-search h2{
    font-family: 'Manrope', sans-serif;
    font-size: 40px;
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