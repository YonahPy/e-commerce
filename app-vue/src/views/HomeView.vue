<template>
  <main>
    <section class="banner">
      <div class="text-banner">
        <h1>EXCITING <strong>PLACE FOR THE WHOLE FAMILY</strong> TO SHOP</h1>
        <p>Here is your chance to upgradeyour wardrobe with a variation of styles and fits that are both</p>
        <button class="shop-now">SHOP NOW <img src="../assets/icons/icons8-sacola-de-compras-64.png" alt="icon-shop" ></button>
      </div>
      <div class="image-baner">
        
      </div>

      
    </section>
    
    <section class="new-arrivals">
     
      
      <div @click="pushToNewArrivals">
        <h2>New Arrivals</h2>
      </div>
      <div class="carousel">
      <carousel :items-to-show="3.3" :autoplay="2000" :wrap-around="true" :transition="500" :products="newArrivals" :pauseAutoplayOnHover="true" @clickedProduct="pushToProduct" >

      </carousel>
    </div>
    </section>

    <section class="best-sellers">
      
      <TabView :women-products="womenBestSellers" :men-products="menBestSellers" @clickedBestSellerProduct="pushToBestSellerProduct">
        
      </TabView>

    </section>
  </main>
</template>

<script>
import axios from 'axios'
import carousel from '../components/Carousel.vue'
import TabView from '../components/TabView.vue';
import { useStore } from '../stores/store'

export default {
  
  components:{
    carousel,
    TabView,
  },
  data(){
    return{
      newArrivals: null,
      womenBestSellers: null,
      menBestSellers: null,
      
    }
  },
  mounted(){
    this.getNewArrivalsProducts()
    this.getWomenBestSellersProducts()
    this.getMenBestSellersProducts()
  },
  
  methods:{
    getNewArrivalsProducts(){
      axios.get(`http://127.0.0.1:8000/api/products/category/${29}/?page=${1}`)
      .then(response => {
        this.newArrivals = response.data.results
      })
      .catch(error => {
        console.log('Erro ao buscar produtos', error)
      })
    },
    getWomenBestSellersProducts(){
      axios.get(`http://127.0.0.1:8000/api/products/category/${27}/?page=${1}`)
      .then(response => {
        this.womenBestSellers = response.data.results
      })
      .catch(error => {
        console.log('Erro ao buscar produtos', error)
      })
    },
    getMenBestSellersProducts(){
      axios.get(`http://127.0.0.1:8000/api/products/category/${28}/?page=${1}`)
      .then(response => {
        this.menBestSellers = response.data.results
      })
      .catch(error => {
        console.log('Erro ao buscar produtos', error)
      })
    },
    
    pushToProduct(idProduct, idCategory, nameCategory){
      this.$router.push(`/product-details/${idProduct}`)
    },
    pushToNewArrivals(){
      useStore().setCategory('New Arrivals', 29)
      this.$router.push('products/')
    },
    pushToBestSellerProduct(idProduct, idCategory, nameCategory){
      this.$router.push(`/product-details/${idProduct}`)
    }
  }
}
  
</script>

<style scoped> 

  .banner{
    display: flex;
    
  }
  .image-baner{
    background-image: url('../assets/baners/pexels-anastasiya-gepp-1462639.jpg');
    background-size: cover;
    
    width: 50vw;
    height: 70vh;
  }
  .text-banner{
    width: 50vw;
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding: 60px;
  }
  .text-banner h1{
    font-family: 'Manrope', sans-serif;
    font-size: 2.5em;
    font-weight: 300;
    margin-bottom: 30px;
  }
  strong{
    font-weight: 900;
  }
  .text-banner p{
    font-family: 'Manrope', sans-serif;
    margin-bottom: 30px;
  }
  .shop-now{
    width: 150px;
    height: 55px;
    font-weight: 900;
    color: white;
    background-color: #171416e8;
    border: none;
    cursor: pointer;
    font-size: 14px;
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 5px;
  }
  .shop-now:hover{
    background-color: #171416;
  }
  .shop-now img{
    height: 35%;
  }

  /* New arrivals*/
  .new-arrivals{
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-top: 80px;
  }
  .new-arrivals h2{
    font-size: 30px;
    margin-bottom: 60px;
    cursor: pointer;
  }
  .carousel{
   width: 80vw;
  }
  
  /* Best Seller*/

  .best-sellers{
    margin-top: 80px;
    margin-bottom: 80px;
  }
 
 @media screen and (max-width: 900px){
  .image-baner{
    width: 50vw;
    height: 55vh;
  }
 }
 @media screen and (max-width: 840px){
  .banner{
    flex-direction: column;
  }
  .image-baner{
   
    width: 100vw;
    height: 70vh;
    background-position: center bottom;
  }
  .text-banner{
    width: 100vw;
    height: 60vh;
  }
 }
</style>


