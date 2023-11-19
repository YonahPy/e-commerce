<template>
<button class="button-cart" :style="buttonStyle">ADD TO CART</button>
</template>

<script>
export default{
    props:{
        width:{
            type: String,
            default: '50%'
        },
        height:{
            type: String,
            default: '50px'
        },
        font:{
            type: String,
            default: '16px'
        }
    },
    computed:{
        buttonStyle(){
            return{
                width: this.width,
                height: this.height,
                fontSize: this.font,
            }
        }
    }
}
</script>

<style scoped>
.button-cart{
    border: none;
    background-color: #171416;
    color: white;
    border-radius: 7px;
    cursor: pointer;
}
.button-cart:hover{
    background-color: #0e0c0e;
    
}
</style>