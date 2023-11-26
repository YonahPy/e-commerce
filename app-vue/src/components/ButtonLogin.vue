<template>
    <button class="login" @click="pushLogin">Login</button>
</template>

<script>
export default{
    methods:{
        pushLogin(){
            this.$router.push('/login')
    }, 
    }
    
}
</script>

<style>
.login {
  background-color: #171416 !important;
  color: white;
  font-size: 16px;
  width: 100px !important;
  height: 40px !important;
  border-radius: 10px;
  
}
.login:hover{
  background-color: #0e0c0d !important;
}
</style>