<template>
<div class="tab-view">
    <div class="header">
        <h2>Best Sellers</h2>

        <div>
            <ul>
                <li @click="showWomenProducts = true">Women</li>
                <li @click="showWomenProducts = false">Men</li> 
                
            </ul>
            
        </div>
        
    </div>
    
    <div class="content">
        <div class="cart" v-for="p in filterBestSellerProducts" :key="p.id">
            <div class="cart-image">
                <img :src="p.image" :alt="p.product_title">
            </div>
            <div class="cart-text">
                <p>{{ p.product_title }}</p>
                <p>{{ p.price }}</p>
            </div>
        </div>
    </div>
</div>
</template>

<script>
export default{
    props:['products'],
    data(){
        return{
            showWomenProducts: true,
            womenProducts: null,
            menProducts:null,
            
        }
    },
    computed:{
        filterBestSellerProducts(){
            if(this.products){
                if (this.showWomenProducts){
                    return this.products.filter((product) => {
                        return product.category === 27
                    }).slice(0, 8)
                } else{
                    return this.products.filter((product) => {
                        return product.category === 28
                    }).slice(0, 8)
                }
            }
            return [];  
        }
    }
}
</script>

<style scoped>
.tab-view{
    margin-inline: 10%;
}
.header{
    display: flex;
    justify-content: space-between;
    
}
ul{
    list-style: none;
    display: flex;
    
}
li{
    margin-right: 25px;
    font-size: 18px;
}
li:hover{
    color: #e49e6c;
    cursor: pointer;
}

</style>