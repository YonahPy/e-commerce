<template>
    <section v-if="token">
        <ProductCard :products="listFavoriteProducts" :show-buttons="true" v-if="token">

        </ProductCard>

        <div v-else>ola mundo</div>
    </section>
    <section v-else class="none-list-favorits">
        <div>
            <h2>Log in to view your favorite product list</h2>

            <div class="icon">
                <img src="../assets/icons/heart_love_add_insert_plus_favourite_icon_178151.svg" alt="heart_love_add_insert_plus_favourite_icon">
            </div>
  
            <div class="buttons">  
                <div>
                    <ButtonLogin :width="'100%'" :height="'100%'">
                    </ButtonLogin>
                </div>
                
                <div>
                    <ButtonRegister :width="'100%'" :height="'100%'">
                    </ButtonRegister>
                </div>

            </div>
        </div>
    </section>

</template>

<script>
import { useStore } from '../stores/store';
import ProductCard from '../components/ProductCard.vue';
import ButtonLogin from '../components/ButtonLogin.vue';
import ButtonRegister from '../components/ButtonRegister.vue';

export default{
    components:{
        ProductCard,
        ButtonLogin,
        ButtonRegister,
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

<style scoped>
.none-list-favorits{
    height: 65vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}
h2{
    font-size: 38px;
    margin-bottom: 20px;
}
.icon{
    display: flex;
    justify-content: center;
}
.icon img{
    width: 15%;
}
.buttons{
  display: flex;  
  align-items: center;
  justify-content: center;
  margin-top: 20px;
}
.buttons div{
    height: 40px;
    width: 150px;
    margin-left: 20px;
}
</style>