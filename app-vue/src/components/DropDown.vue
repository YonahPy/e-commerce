<template>
    <div class="dropdown">
        <p v-for="category in categories" :key="category.id" @click="changeCategory(category.name, category.id)">
            {{ category.name }}           
        </p>        
    </div>
    
</template>

<script>
import {useStore} from '../stores/store'


export default{
    props: ['categories'],
    methods:{
        changeCategory(name, id){
            useStore().setCategory(name, id);
            this.$router.push('/products')
        }
    }
}
</script>

<style scoped>
.dropdown{
    display: flex;
    flex-direction: column;
    background-color: #171416;
    width: 200px;
    border-radius: 10px;
    padding: 15px;
    border: 2px solid #373536;
    
}
.dropdown p{
    color: white;
    font-size: 15px;
    margin-bottom: 8px;
    cursor: pointer;
}
.dropdown p:hover{
    color: #e49e6c;
}

@media screen and (max-width: 780px){
    .dropdown{
        width: 110%;
        margin-top: 20px;
    }
}
</style>

