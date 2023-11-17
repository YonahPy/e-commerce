<template>
    <carousel>
      <slide v-for="p in firstTenProducts" :key="p.id">
        <div class="carousel__item" @click="handleClick(p.id, p.category, p.name_category)">
            <div>
                <img :src="p.image" alt="">
            </div>
            <div class="carousel-text">
                <p>{{ p.product_title }}</p>
                <p class="price">R$ {{ p.price }}</p>
                
            </div>
        </div>
        
      </slide>
  
      <template #addons>
        <navigation />
        <pagination />
      </template>
    </carousel>
  </template>
  
  <script>
  
  import 'vue3-carousel/dist/carousel.css'
  import { Carousel, Slide, Pagination, Navigation } from 'vue3-carousel'
  import { useStore } from '../stores/store';
import axios from 'axios';
  
  export default {
    name: 'App',
    components: {
      Carousel,
      Slide,
      Pagination,
      Navigation,
    },
    props:['products'],

    emits:['clickedProduct'],

    computed: {
    firstTenProducts() {
        if (this.products) {
            return this.products.slice(5, 15);
      } else {
            return [];
      }
      
    },
    
  },
  methods:{
    
    handleClick(idProduct, idCategory, nameCategory){
      this.$emit('clickedProduct', idProduct, idCategory, nameCategory)

      useStore().setCategory(nameCategory, idCategory)
        
      }  
      
  }

  }
  </script>

<style scoped>

.carousel-text p{
  font-size: 13px;
  margin-top: 7px;
}
.carousel__item{
  cursor: pointer;
}
.price{
  font-weight: bold;
}
.carousel__slide {
  padding: 25px;
  
}

.carousel__viewport {
  perspective: 2000px;
  
}

.carousel__track {
  transform-style: preserve-3d;
}

.carousel__slide--sliding {
  transition: 0.5s;
}

.carousel__slide {
  opacity: 0.9;
  transform: rotateY(-20deg) scale(0.9);
}

.carousel__slide--active ~ .carousel__slide {
  transform: rotateY(20deg) scale(0.9);
}

.carousel__slide--prev {
  opacity: 1;
  transform: rotateY(-10deg) scale(0.95);
}

.carousel__slide--next {
  opacity: 1;
  transform: rotateY(10deg) scale(0.95);
}

.carousel__slide--active {
  opacity: 1;
  transform: rotateY(0) scale(1.1);
}

</style>