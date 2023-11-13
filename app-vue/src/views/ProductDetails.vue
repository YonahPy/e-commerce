<template>
    <section v-if="products">
        <div class="image-product">
            <img v-if="products.alternative_image" :src="products.alternative_image" :alt="products.product_title" >

            <img v-else :src="products.image" :alt="products.product_title" >
        </div>

        <div>
            <div>
                <h2>{{products.product_title }}</h2>
                <p>{{products.price }}</p>
            </div>
            <div>
                <h3>Color</h3>

            </div>
            <div class="buttons-add">
                <button>ADD TO CART</button>
                <button><img src="../assets/icons/love.png" alt="icon-favorite"></button>
            </div>
            
        </div>
    </section>
</template>

<script>
import axios from 'axios';

export default{
    data(){
        return{
            products: null
        }
    },
    mounted(){
        const productId = this.$route.params.id;
        this.getDataProducts(productId)
    },
    methods:{
        getDataProducts(productId){
            axios.get(`http://127.0.0.1:8000/api/products/${productId}/`)
            .then(response => {
                this.products = response.data
            })
            .catch(error => {
                console.log('Erro ao buscar os dados', error)
            })
        }
    },
}
</script>

<style scoped>
.image-product img{
    width: 100%;
}
</style>