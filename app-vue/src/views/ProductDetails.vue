<template>
    <section v-if="products" class="section-product">
        <div class="product-image">
            <img v-if="products.alternative_image" :src="products.alternative_image" :alt="products.product_title" >

            <img v-else :src="products.image" :alt="products.product_title">
        </div>

        <div>
            <div class="product-info">
                <h2>{{products.product_title }}</h2>

                <div class="rating-line">
                    <div class="icon-rating">
                        <img src="../assets/icons/star-346.svg" alt="icon-reviews">
                    </div>
                    <p v-if="products.average_rating">{{ products.average_rating  }}</p>
                    <p v-else>4.2</p>
                    <p v-if="products.count_rating">({{ products.count_rating }})</p>
                    <p v-else>(822)</p>
                </div>

                <p class="price">R$ {{products.price }}</p>
                
            </div>
            <div class="product-color">
                <h3>Color</h3>
               
                <div class="colors">
                    <div v-for="color in products.color" class="selected-color">
                        <img :src="color.url" :alt="color.color">
                    </div>
                </div>
                
            </div>
            <div class="buttons-add">
                <button class="button-cart">ADD TO CART</button>
                <button class="button-favorite">
                    <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" width="256" height="256" viewBox="0 0 256 256" xml:space="preserve">
                    <defs>
                    </defs>
                    <g style="stroke: none; stroke-width: 0; stroke-dasharray: none; stroke-linecap: butt; stroke-linejoin: miter; stroke-miterlimit: 10; fill: none; fill-rule: nonzero; opacity: 1;" transform="translate(1.4065934065934016 1.4065934065934016) scale(2.81 2.81)" >
                        <path d="M 84.646 11.504 C 75.554 1.233 58.335 -0.041 45 13.074 C 31.665 -0.041 14.446 1.233 5.354 11.504 c -9.671 10.926 -5.609 31.318 7.123 47.615 C 18.931 67.38 34.874 80.832 45 86.481 c 10.126 -5.649 26.069 -19.101 32.523 -27.362 C 90.255 42.822 94.318 22.43 84.646 11.504 z" style="stroke: none; stroke-width: 1; stroke-dasharray: none; stroke-linecap: butt; stroke-linejoin: miter; stroke-miterlimit: 10; fill: rgb(248,48,95); fill-rule: nonzero; opacity: 1;" transform=" matrix(1 0 0 1 0 0) " stroke-linecap="round" />
                    </g>
                    </svg>
                </button>
            </div>
            
        </div>
    </section>
    <section>
        <div class="similar-products">
            <h2>Similar Products</h2>
            
        </div>
        <div class="similar-products-carousel">
            <carousel :items-to-show="3.3" :autoplay="2000" :wrap-around="true" :transition="500" :products="productsCarousel" :pauseAutoplayOnHover="true" @clickedProduct="renderProduct" >

            </carousel>
        </div>
    </section>
</template>

<script>
import axios from 'axios';
import carousel from '../components/Carousel.vue';
import { useStore } from '../stores/store';



export default{
    components:{
        carousel
    },
    data(){
        return{
            products: null,
            productsCarousel: null,
            idCategoryOfCurrentProduct: null,
            nameCategoryOfCurrentProduct: null
        }
    },
    mounted(){
        const productId = this.$route.params.id;
        this.getDataProducts(productId)
        const store = useStore()
        this.getProductsFromCurrentCategory(store.idCurrentCategory)
    },
    updated(){
        const store = useStore()
        store.setCategory(this.nameCategoryOfCurrentProduct, this.idCategoryOfCurrentProduct)
        this.getProductsFromCurrentCategory(store.idCurrentCategory)
    },
    methods:{
        getDataProducts(productId){
            axios.get(`http://127.0.0.1:8000/api/products/${productId}/`)
            .then(response => {
                this.products = response.data;
                this.idCategoryOfCurrentProduct = this.products.category;
                this.nameCategoryOfCurrentProduct = this.products.name_category;
                
            })
            .catch(error => {
                console.log('Erro ao buscar os dados', error)
            })
        },
        getProductsFromCurrentCategory(categoryId){
            axios.get(`http://127.0.0.1:8000/api/products/category/${categoryId}/`)
            .then(response => {
                this.productsCarousel = response.data
            })
            .catch(error => {
                console.log('Erro ao buscar os dados', error)
            })
        },
        renderProduct(idProduct, idCategory, nameCategory){
            this.$router.push(`/product-details/${idProduct}`)
            this.getDataProducts(idProduct)
        }
    },
}
</script>

<style scoped>
.section-product{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 30px;
    margin-inline: 4vw;
    margin-block: 40px; 
}

.product-image img{
    width: 100%;
    height: 90%;
}
.product-info h2{
    font-family: 'Manrope', sans-serif;
    font-size: 30px;
    margin-bottom: 15px;
}
.price{
    font-weight: bold;
    font-size: 22px;
    margin: 10px 0px 30px 0px;
}
.rating{
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-top: 10px;
}
.rating-line{
    display: flex; 
    width: 50%;
    align-items: center;
}
.rating-line p{
    margin-left: 5px;
}
.icon-rating{
    width: 7%;
}
.icon-rating img{
    width: 100%;
}
.product-color h3{
    font-family: 'Manrope', sans-serif;
    font-size: 22px;
    margin-bottom: 15px;
}
.colors{
    display: flex;
    flex-direction: row;
    gap: 7px;

}
.colors img{
    width: 20px;
    height: 20px;
}
.colors img:hover{
    border: 2px solid #e49e6c;
    cursor: pointer;
}
.buttons-add{
    display: flex;
    align-items: center;
    margin-top: 30px;
}
.buttons-add button{
    height: 50px;
    border-radius: 7px;
    cursor: pointer;
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

.button-cart{
    border: none;
    background-color: #171416;
    color: white;
    font-size: 16px;
    width: 50%;
}
.button-cart:hover{
    background-color: #0e0c0e;
    
}
.button-favorite{
    width: 15%;
    border: 1px solid #171416;
    margin-left: 15px;
}
.similar-products-carousel{
   margin-inline: 4vw;
    
}
.similar-products h2{ 
    margin-inline: 4vw;
    font-size: 30px;
    
}
.similar-products{
    margin-bottom: 15px;
}
</style>