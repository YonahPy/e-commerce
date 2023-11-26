<template>
    <section>
        <form @submit.prevent="registerUser" method="post">
            <h2>Register</h2>
            <div class="username">
                <label for="username">Username</label>
                <br>
                <input type="text" placeholder="Username" required id="username" name="username" v-model="username" maxlength="200">  
            </div>
            
            <div class="email">
                <label for="email">Email</label>
                <br>
                <input type="email" placeholder="Email" required id="email" name="email" v-model="email" maxlength="200">
            </div>
            <div class="password">
                <label for="password">Password</label>
                <br>
                <input type="password" required placeholder="Password" id="password" name="password" v-model="password" maxlength="200">
            </div>
            <span>{{ message }}</span>
            <div class="buttons">
                <input type="submit" value="Enter"  :disabled="disableButton">
            
                <div class="register">
                    <button @click="pushLogin">Login</button>
                </div>
            </div>
            
        </form>
    </section>
</template>

<script>
import axios from 'axios';
import { useStore } from '../stores/store'

export default{
    data(){
        return{
            username: '',
            password: '',
            email: '',
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
        pushLogin(){
            this.$router.push('/login')
        },
        async registerUser(){
            this.disableButton = true

            try{
                const response = await axios.post('http://127.0.0.1:8000/api-auth/register/', {
                    username: this.username,
                    password: this.password,
                    email: this.email
                });
                this.message = ''
                useStore().setToken(response.data)
                this.$router.push('/')
            } catch (error){
                console.log('Erro no registro', error.response.data);
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