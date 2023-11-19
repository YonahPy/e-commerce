<template>
    <section>
        <ProductCard :products="listFavoriteProducts" :show-buttons="true">

        </ProductCard>
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
        }
    }
}
</script>

<style>

</style>