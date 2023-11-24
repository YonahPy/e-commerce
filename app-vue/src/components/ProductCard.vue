<template>
    <div class="products">
        
        <div class="cart-products" v-for="product in products" :key="product.id">
            <RouterLink :to="{name:'productDetails', params:{id: product.id}}" >
                <div class="cart-image">
                <img :src="product.alternative_image" :alt="product.product_title" v-if="product.alternative_image">
                <img :src="product.image" :alt="product.product_title" v-else>
                </div>
                <div class="cart-info">
                    <p>{{ product.product_title }}</p>
            
                    <div class="rating">
                        <div class="rating-line">
                            <div class="icon-rating">
                                <img src="../assets/icons/star.png" alt="icon-reviews">
                            </div>
                            <p v-if="product.average_rating">{{ product.average_rating  }}</p>
                            <p v-else>4.2</p>
                            <p v-if="product.count_rating">({{ product.count_rating }})</p>
                            <p v-else>(822)</p>
                        </div>
                        <p class="price">R$ {{ product.price }}</p>
                    </div>
                </div>
            
            </RouterLink>
            <div class="buttons" v-if="showButtons">
                <ButtonDelete :width="'40%'" :font="'13px'" :height="'40px'"  :product="product.id">
                </ButtonDelete>
                <AddCart :width="'40%'" :font="'13px'" :height="'40px'" :products="products">
                </AddCart>
            </div>  
        </div>
    </div>
</template>

<script>
import { RouterLink } from 'vue-router';
import ButtonDelete from '../components/ButtonDelete.vue';
import AddCart from '../components/AddCart.vue';

export default{
    components:{
        RouterLink,
        ButtonDelete,
        AddCart,
    },
    props:{
        products:{
            type: Object,
            required: true
        },
        showButtons:{
            type: Boolean,
            default: false
        }
    }
}
</script>

<style scoped>

.products{
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    margin-inline: 4vw;
    gap: 70px;
    
}

.cart-image img{
    width: 100%;
    margin-bottom: 10px;
}


.cart-info p{
    margin-top: 5px;
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
    align-items: end;
}
.rating-line p{
    margin-left: 5px;
}
.icon-rating{
    width: 11%;
}
.icon-rating img{
    width: 100%;
}
.price{
    margin-right: 20px;
}
.buttons{
    display: flex;
    justify-content: space-between;
    margin-top: 15px;
    padding-right: 15px;
    
}
</style>