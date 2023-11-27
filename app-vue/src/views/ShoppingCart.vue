<template>
    <section>
        
        <div v-if="token">
            
            <div class="titles">
                <h3>Product</h3>
                <h3>Price</h3>
                <h3>Amount</h3>
                <h3>Total</h3>
            </div>
            
            <div class="container">
                <div>
                    <div v-for="product in cartList" :key="product.id" class="products">
                        <div class="cart-list">
                            <div class="info-product">
                                <div class="image-product">
                                    <button @click="deleteProduct(product.id)" class="delete-button">x</button>
                                    <img :src="product.image" :alt="product.product_title">
                                </div>
                                <div class="name-product">{{ product.product_title }}</div>
                            </div>
                            <div class="price-product">
                                <div>R$ {{ product.price }}</div>
                            </div>
                            <div class="amount-product">
                                <button @click="decreaseCount(product)">-</button>
                                <span class="count">{{ product.quantity }}</span>
                                <button @click="increaseCount(product)">+</button>
                            </div>
                            <div class="total-price">
                                <div>R$ {{ calculateTotal(product) }}</div>
                            </div>
                        </div>
                        <div class="line"></div>
                    </div>
                    
                </div>
                <div class="total-pay">
                    <p class="cart-total">CART TOTAL <strong>  R$ {{ totalAmount }}</strong></p>
                    <p>Shipping & taxes calculated at checkout</p>

                    <Checkout class="checkout">

                    </Checkout>
                </div>
            </div>
            
        </div>

        <div v-else class="none-cart-list">
            <div>
            <h2>Log in to view your shopping cart</h2>

            <div class="icon">
                <img src="../assets/icons/shoppingcart_120371.svg" alt="shoppingcart">
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
            </div>
    </section>
</template>

<script>
import { useStore } from '../stores/store';
import Checkout from '../components/CheckoutButton.vue'
import ButtonLogin from '../components/ButtonLogin.vue';
import ButtonRegister from '../components/ButtonRegister.vue';

export default{
    components:{
        Checkout,
        ButtonLogin,
        ButtonRegister,
    },
    data(){
        return{
            cartList: useStore().listShoppingCart,

        }
    },
    computed:{
        totalAmount(){
            return this.cartList.reduce((total, product) => {
                return total + this.calculateTotal(product)
            }, 0)
        },
        token(){
            return useStore().token
        }

    },
    methods:{
        increaseCount(product){
            product.quantity++
            this.recalculateTotal(product);
            
        },
        decreaseCount(product){
            if(product.quantity > 1){
                product.quantity--
                this.recalculateTotal(product);
            }
        },
        calculateTotal(product) {
            return product.price * product.quantity;
        },
        recalculateTotal(product) {
            const updatedTotal = this.calculateTotal(product);
      
        },
        deleteProduct(idProduct){
            useStore().deleteItemFromShoppingCart(idProduct)
        }
    }
    
}
</script>

<style scoped>
.line{
    height: 2px;
    background-color: #d4cdd4;
    width: 80%;
    margin-inline: 4vw;
    margin-top: 30px;
   
}
.products{
    display: flex;
    flex-direction: column;
}

.container{
    display: grid;
    grid-template-columns: 80% 20%;
}
.titles{
    display: flex;
    margin-left: 4vw;
    align-items: center;
    width: 80%;
}
h3{
    font-family: 'Manrope', sans-serif;
}
.titles h3{
    width: 22%;
    font-size: 25px;
    margin-top: 30px;
}
.cart-list{
    display: flex;
    margin-inline: 4vw;
    margin-top: 50px;
    align-items: center;
}
.info-product{
    width: 25%;
    padding-right: 30px;
}
.name-product{
    font-size: 14px;
}
.delete-button{
    color: white;
    background-color: #ff4e3e;
    border: none;
    border-radius: 50%;
    width: 20px;
    height: 20px;
    text-align: center;
    font-weight: bold;
    cursor: pointer;
    position: absolute;
    right: 0;
    top: 10px;
}
.image-product{
    width: 120px;
    margin-bottom: 15px;
    position: relative;
    padding-top: 15px;
}
.image-product img{
    width: 100%;
}
.price-product{
    width: 25%;
    font-size: 20px;
}
.amount-product{
    width: 25%;
}
.amount-product button{
    width: 40px;
    border: 1px solid #171416;
    font-size: 25px;
    background-color: transparent;
    color: #171416;
    border-radius: 20px;
    cursor: pointer;
}
.amount-product button:hover{
    background-color: #d4cdd4;
}
.count{
    margin-inline: 10px;
    font-size: 20px;
    font-weight: bolder;
}
.total-price{
    width: 25%;
    font-size: 20px;
}
.total-pay{
    border: 1px solid #908d90;
    padding: 20px;
   height: 300px;
    margin-right: 10px;
    border-radius: 10px;
    background-color: #d4cdd4;
    position: fixed;
    right: 0;
    

}
.total-pay p{
    letter-spacing: 2px;
    
}
.checkout{
    margin-top: 25px;
}
.cart-total{
    margin-bottom: 10px;
}
strong{
    font-size: 22px;
}


.none-cart-list{
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
    width: 20%;
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