<template>
    <div class="login-div" :style="{'width': width, 'height': height}">
      <button class="login" @click="pushLogin" :style="{'background-color': backgroundColor, 'color': color}">Login</button>
    </div>
</template>

<script>
export default{
    props:{
        width: String,
        height: String,
        backgroundColor: String,
        color: String,
    },
    methods:{
        pushLogin(){
            this.$router.push('/login')
    }, 
    }
    
}
</script>

<style scoped>
.login-div{
  width: 40%;
  
}
.login {
  background-color: #171416 ;
  color: white;
  font-size: 16px;
  width: 100%;
  height: 100%;
  border-radius: 7px;
  border: none;
  cursor: pointer;
  
}
.login:hover{
  background-color: #0e0c0d;
}
</style>