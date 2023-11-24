<template>
    <section>
        <form action="#">
            <h2>Register</h2>
            <div class="username">
                <label for="username">Username</label>
                <br>
                <input type="text" placeholder="Username" required>
            </div>
            <div class="genrer-age">
                <div class="age">
                    <label for="age">Age</label>
                    <br>
                    <input type="date">
                </div>
                <div class="genrer">
                    <label for="genrer">Genrer</label>
                    <br>
                    <select name="genrer" id="genrer">
                        <option value="Male">Male</option>
                        <option value="female">Female</option>
                    </select>
                </div>
            </div>
            <div class="email">
                <label for="email">Email</label>
                <br>
                <input type="email" placeholder="Email" required>
            </div>
            <div class="password">
                <label for="password">Password</label>
                <br>
                <input type="password" required placeholder="Password">
            </div>
            <div class="buttons">
                <input type="submit" value="Enter">
            
                <div class="register">
                    <button @click="pushLogin">Login</button>
                </div>
            </div>
            
        </form>
    </section>
</template>

<script>
export default{
    methods:{
        pushLogin(){
            this.$router.push('/login')
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
.genrer-age{
    display: flex;
}
.age{
    width: 25%;
    margin-right: 5%;
}
.age input{
    width: 100%;
    
}
.genrer{
    width: 30%;
}
.genrer-age select{
    border: none;
    height: 40px;
    padding-left: 10px;
    font-size: 17px;
    border-radius: 5px;
    border: 1px solid #171416;
    margin-top: 10px;
    width: 100%;
    
}
</style>