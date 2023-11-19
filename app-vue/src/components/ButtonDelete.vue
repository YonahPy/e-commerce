<template>
<button class="button-delete" :style="buttonStyle" @click="deleteProductFromFavoriteList">DELETE</button>
</template>

<script>
import { useStore } from '../stores/store';

export default{
    props:{
        product:{
            type: Number
        },
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
    },
    methods:{
        deleteProductFromFavoriteList(){
            useStore().deleteItemFromFavoriteList(this.product)
        }
    }
}

</script>

<style scoped>
.button-delete{
    height: 50px;
    border-radius: 7px;
    cursor: pointer;
    border: 1px solid #ff4e3e;
    color: #ff4e3e;
    background-color: transparent;
}
.button-delete:hover{
    background-color:#ff4e3e ;
    color: white;
    transition: background 0.2s ease;
}
</style>