<template>
    <section class="note">
        <p>Name: {{ username }}</p>
        <p>Email: {{ email }}</p>
        <p>Total Value: {{ totalPrice }}</p>

        <div class="image">
            <img src="../assets/icons/checked.png" alt="checked icon">
        </div>
        <p class="pay">Payment made successfully</p>
    </section>
</template>

<script>
import { useStore } from '../stores/store';
import axios from 'axios';

export default{
    data(){
        return{
            username: '',
            email: '',
            data: null,
        }
    },
    mounted(){
        this.getUserInfomation()
    },
    computed:{
        totalPrice(){
            return useStore().totalPrice;
        },
        token(){
            return useStore().token;
        }
    },
    methods:{
        async getUserInfomation(){
            try{
                const response = await axios.get('http://127.0.0.1:8000/api-auth/user/', {
                headers:{
                    Authorization: `Token ${this.token}`
                } 
                })
                
                this.username = response.data.name
                this.email = response.data.email
                           
            } catch(error){
                console.log(error)
            }
            
        }

}
}
</script>

<style scoped>
.note{
    height:50vh;
    width: 30vw;
    border-radius: 10px;
    margin: 0 auto;
    margin-top: 5vh;
    background-color: rgb(204, 195, 195);
    border: 2px solid #171416;
    padding: 15px;
}
.image{
    margin: 0 auto;
    margin-top: 50px;
    width: 20%;
}
.image img{
    width: 100%;
}
.pay{
    text-align: center;
    margin-top: 10px;
}
.note p{
    font-size: 18px;
    margin-bottom: 10px;
}
</style>