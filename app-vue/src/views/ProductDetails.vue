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
                <AddCart :products="products" v-if="token">

                </AddCart>
                
                <AddFavorite :products="products" v-if="token">
                    
                </AddFavorite>
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
import AddFavorite from '../components/AddFavorite.vue';
import AddCart from '../components/AddCart.vue';


export default{
    components:{
        carousel,
        AddFavorite,
        AddCart,
    },
    data(){
        return{
            products: null,
            productsCarousel: null,
            idCategoryOfCurrentProduct: null,
            nameCategoryOfCurrentProduct: null,
            
        }
    },
    mounted(){
        const productId = this.$route.params.id;
        this.getDataProducts(productId)
        const store = useStore()
        this.getProductsFromCurrentCategory(store.idCurrentCategory)
    },
    watch:{
        idCategoryOfCurrentProduct(newId, oldId){
            const store = useStore();
            if(newId !== oldId){
                store.setCategory(this.nameCategoryOfCurrentProduct, newId);
                this.getProductsFromCurrentCategory(newId)
            }        
        }
    },
    computed:{
        token(){
            return useStore().token
        }
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
                this.productsCarousel = response.data.results
            })
            .catch(error => {
                console.log('Erro ao buscar os dados', error)
            })
        },
        renderProduct(idProduct, idCategory, nameCategory){
            this.$router.push(`/product-details/${idProduct}`)
            this.getDataProducts(idProduct)
        },
        
        
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