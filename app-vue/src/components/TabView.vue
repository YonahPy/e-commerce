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
        
        <div class="cart" v-for="p in filterBestSellerProducts" :key="p.id" @click="handleClick(p.id, p.category, p.name_category)">
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
    props:['womenProducts', 'menProducts'],
    emits:['clickedBestSellerProduct'],
    data(){
        return{
            showWomenProducts: true,
                
        }
    },
    computed:{
        filterBestSellerProducts(){
            if(this.womenProducts && this.menProducts){
                if (this.showWomenProducts){
                    return this.womenProducts.slice(0, 8)
                } else{
                    return this.menProducts.slice(0, 8)
                }
            }
            return [];  
        }   
    },
    methods:{
        handleClick(idProduct, idCategory, nameCategory){
            this.$emit('clickedBestSellerProduct', idProduct, idCategory, nameCategory)
            useStore().setCategory(nameCategory, idCategory)
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
.cart{
    cursor: pointer;
}

.cart-image{
    width: 100%;
    display: flex;
    justify-content: center;
    
}
.cart-image img{
    width: 210px;
    height: 190px;
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