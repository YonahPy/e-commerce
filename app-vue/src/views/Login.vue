<template>
    <section>
        <form method="post" @submit.prevent="loginUser">
            <h2>Login</h2>
            <div class="email">
                <label for="email">Username</label>
                <br>
                <input type="text" placeholder="Username" required v-model="username" id="username" name="username" maxlength="200">
            </div>
            <div class="password">
                <label for="password">Password</label>
                <br>
                <input type="password" required placeholder="Password" v-model="password" name="password" id="password" maxlength="200">
            </div>
            <span>{{ message }}</span>
            <div class="buttons">
                <input type="submit" value="Enter" :disabled="disableButton">

            
                <div class="register">
                    <button @click="pushRegister">Register</button>
                </div>
            </div>
            
        </form>
    </section>
</template>

<script>
import axios from 'axios';
import {useStore} from '../stores/store'

export default{
    data(){
        return{
            username: '',
            password: '',
            message: '',
            disableButton: true
        }
    },
    
    computed:{
        validationForm(){
            const passwordRegex = /^(?=.*[0-9])(?=.*[!@#$%^&*])[a-zA-Z0-9!@#$%^&*]{8,}$/;

            if (!this.password) {
                this.message = 'Password cannot be empty';
            } else if (this.password.length < 8){
                this.message = 'Password should contain at least 8 characters';
            } else if (!passwordRegex.test(this.password)){
                this.message = 'Password should contain at least 1 number and 1 special character';
            } else{
                this.message = ''
                this.disableButton = false
            }
        }
    },
    watch:{
        password(){
            this.validationForm           
        }
    },
    methods:{
        pushRegister(){
            this.$router.push('/register')
        },
        async loginUser(){
            this.disableButton = true

            try{
                console.log(this.username, this.password)
                const response = await axios.post('http://127.0.0.1:8000/api-auth/login/', {
                    username: this.username,
                    password: this.password,
                });
                this.message = ''
                console.log(response.data)
                useStore().setToken(response.data)
                this.$router.push('/')
            } catch (error){
                console.log('Erro no registro', error);
                this.message = error.response.data.error
            } finally{
                this.disableButton = false
            }
            

        }
    }
}
</script>

<style scoped>
form{
    
    width: 70vw;
    margin: 0 auto;
    border-radius: 10px;
    padding: 60px 0px 60px 20px;
    margin-block: 10vh;
}
h2{
    font-size: 30px;
    font-family: 'Manrope', sans-serif;
    margin-bottom: 20px;
}
div label{
    font-size: 18px;

}
div input{
    margin: 10px 0px;
}
div input, button{
    border: none;
    height: 40px;
    padding-left: 10px;
    font-size: 17px;
    border-radius: 5px;
    width: 60%;
    border: 1px solid #171416;
}
div input:focus{
    border: 1px solid #e49e6c;
    outline: none;
}
.buttons{
    width: 60%;
    display: flex;
}
.buttons input{
    width: 40%;
    background-color: #171416;
    color: white;
    font-size: 18px;
    letter-spacing: 2px;
    cursor: pointer;
    margin-right: 40px;
}
.buttons input:hover{
    background-color: #0e0c0d;
}
.buttons .register{
    width: 40%;
    
}
.buttons .register button{
    width: 100%;
    margin-top: 10px;
    background-color: white;
    font-size: 18px;
    border: 1px solid #0e0c0d;
    cursor: pointer;
}
.buttons .register button:hover{
    background-color: #171416;
    color: white;
}
</style>