<template>
<div class="tab-view">
    <div class="header">
        <h2>Best Sellers</h2>

        <div>
            <ul>
                <li @click="showWomenProducts = true" :class="{'isactive': showWomenProducts}">Women</li>
                <li @click="showWomenProducts = false" :class="{'isactive': !showWomenProducts}">Men</li> 
                
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
                <p class="price">R$ {{ p.price }}</p>
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
.isactive{
    color: #e49e6c;
    text-decoration: underline #e49e6c;
    text-underline-offset: 10px;
    text-decoration-thickness: 2px;
}
.tab-view{
    margin-inline: 10%;
}
.header{
    display: flex;
    justify-content: space-between;
    margin-bottom: 60px;
}
.header h2{
    font-size: 30px;
}
.content{
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 20px;
}

.cart-image{
    width: 100%;
    display: flex;
    justify-content: center;
    
}

.cart-text p{
    font-size: 13px;
    margin-top: 7px;
}

.price{
    font-weight: bold;
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