<template>
    <section v-if="token">
        <ProductCard :products="listFavoriteProducts" :show-buttons="true" v-if="token">

        </ProductCard>

        <div v-else>ola mundo</div>
    </section>

</template>

<script>
import { useStore } from '../stores/store';
import ProductCard from '../components/ProductCard.vue';

export default{
    components:{
        ProductCard,
    },
    computed:{
        listFavoriteProducts(){
            const store = useStore().listFavoriteProducts;
            return store
        },
        token(){
            return useStore().token
        }
    }
}
</script>

<style>

</style>