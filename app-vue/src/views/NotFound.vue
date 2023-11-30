<template>
    <div class="none-cart-list">
        <div>
            <h2>Page not found</h2>

            <div class="icon">
                <img src="../assets/icons/no-connection.png" alt="shoppingcart">
            </div>
  
            <div class="buttons">  
                <button @click="pushHome"><img src="../assets/icons/undo.png" alt=""> Home</button>

            </div>
        </div>
    </div>
</template>

<script>
export default{
    methods:{
        pushHome(){
            this.$router.push('/')
        }
    }
}

</script>

<style scoped>
.none-cart-list{
    height: 65vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
}
h2{
    font-size: 50px;
    margin-bottom: 50px;
}
.icon{
    display: flex;
    justify-content: center;
}
.icon img{
    width: 30%;
}
.buttons{
    display: flex;
    justify-content: center;
}
button{
    margin-top: 50px;
    width: 150px;
    background-color: transparent;
    border: 2px solid #171416;
    height: 50px;
    border-radius: 5px;
    font-size: 17px;
    color: #171416;
    cursor:  pointer;
    font-weight: bold;
    display: flex;
    align-items: center;
    justify-content: center;
}

.buttons button:hover{
    background-color: rgb(163, 160, 160);

}

.buttons button img{
    width: 18%;
    margin-right: 10px;
}
</style>