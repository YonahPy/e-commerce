<template>
    <section class="checkout">
        <div class=".checkout-container">
            <h2>Checkout</h2>
            <form id="checkout-form" method="post" @submit.prevent="dataCheckout">
                <div class="name">
                  <div>
                    <label for="first-name">First Name:</label>
                    <input type="text" id="first-name" name="first-name" placeholder="Enter first name" required v-model="firstName">
                  </div>
                  <div>
                    <label for="last-name">Last Name:</label>
                    <input type="text" id="last-name" name="last-name" placeholder="Enter last name" required v-model="lastName">
                  </div>
                </div>
                <label for="username">Username:</label>
                <input type="text" id="username" name="username" placeholder="Enter username" required v-model="username">
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" placeholder="Enter email" required v-model="email">
                <label for="address">Address:</label>
                <input type="text" id="address" name="address" placeholder="Enter address" required v-model="adress">
                <div class="name">
                  <div>
                    <label for="city">City</label>
                    <input type="text" id="city" name="city" placeholder="Enter city" required v-model="city">
                  </div>
                  <div>
                    <label for="state">State:</label>
                    <input type="text" id="state" name="state" placeholder="Enter state" required v-model="state">
                  </div>
                </div>
                <label for="card-number">Card Number:</label>
                <input type="text" id="card-number" name="card-number" placeholder="Enter card number" maxlength="16" required v-model="cardNumber">
                <div class="name">
                  <div>
                    <label for="expiration">Expiration Date:</label>
                    <input type="text" id="expiration" name="expiration" placeholder="MM/YYYY" pattern="(0[1-9]|1[0-2])\/[0-9]{4}" required v-model="expiration">
                  </div>
                  <div>
                    <label for="cvv">CVV:</label>
                    <input type="text" id="cvv" name="cvv" placeholder="CVV" maxlength="3" required v-model="cvv">
                  </div>
                </div>
                <span class="message">{{ message }}</span>
                <CheckoutButton>
                  
                  Submit Payment
                </CheckoutButton>
            </form>
        </div>
    </section>
</template>

<script>
import axios from 'axios'
import { useStore } from '../stores/store';
import { computed } from 'vue';
import CheckoutButton from '../components/CheckoutButton.vue';

export default{
  components:{
    CheckoutButton
  },
  data(){
    return{
      message: '',
      firstName: '',
      lastName: '',
      username: '',
      email: '',
      adress:'',
      city: '',
      state: '',
      cardNumber: null,
      expiration: '',
      cvv: '',
      total: null,
    }
  },
  computed:{
      token(){
        return useStore().token
      },
    },
  methods:{
    async dataCheckout(){
      try{
        const response = await axios.post('http://127.0.0.1:8000/api/checkout/checkout/',{
          firstName:this.firstName,
          lastName: this.lastName,
          username: this.username,
          email: this.email,
          adress: this.adress,
          city: this.city,
          state: this.state,
          cardNumber: this.cardNumber,
          expiration: this.expiration.toString(),
          cvv: this.cvv,
        }, {
          headers:{
            Authorization: `Token ${this.token}`
          }
        })
        if (response.status === 200){
          this.$router.push('/successful-payment');
          this.message = '';
          useStore().isPaymentComplete = true
        }
      } catch (error){
          console.log('Erro ao enviar os dados', error);
          this.message = error.response.data.error;
      }
      
    },
    
  }
}
</script>

<style>
.message{
  color: #ff4e3e;
  font-size: 18px;
  margin-bottom: 15px;
}
.checkout {
  font-family: Arial, sans-serif;
  margin: 0 auto;
  padding: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  width: 80vw;

}

.checkout-container {
  border-radius: 8px;
  padding: 20px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

h2 {
  text-align: center;
  font-size: 40px;
  margin-block: 40px;
}

form {
  display: flex;
  flex-direction: column;
}

label {
  margin-bottom: 8px;
}

input[type="email"],
input[type="text"] {
  width: calc(100% - 22px);
}


input[type="text"],
input[type="email"],
button {
  padding: 10px;
  margin-bottom: 15px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

input[type="text"]:focus,
input[type="email"]:focus,
button:focus {
  outline: none;
  border-color: #66afe9;
  box-shadow: 0 0 5px #66afe9;
}

button {
  background-color: #66afe9;
  color: white;
  cursor: pointer;
  font-size: 16px;
}

button:hover {
  background-color: #5a98d6;
}
.name{
  display: flex;
 
}
</style>