<template>
    <div class="register" :style="{'width': width, 'height': height}">
        <button @click="pushRegister">Register</button>
    </div>
</template>

<script>
export default{
    props:{
        width: String,
        height: String,
    },
    methods:{
        pushRegister(){
                this.$router.push('/register')
            },
    }
}

</script>

<style scoped>
.register{
    width: 40%;
    
}
button{
    width: 100%;
    height: 100%;
    background-color: white;
    font-size: 18px;
    border: 1px solid #0e0c0d;
    cursor: pointer;
    border-radius: 7px;
}
button:hover{
    background-color: #171416;
    color: white;
}
</style>