<template>
    <div class="user-options">
        <button @click="logout">Logout</button>
    </div>
</template>

<script>
import axios from 'axios';
import { useStore } from '../stores/store';

export default{
    methods:{
        async logout(){
            let token = useStore().token;

            try{               
                if(token){
                    const response = await axios.post('http://127.0.0.1:8000/api-auth/logout/', {}, {
                        headers: {
                            Authorization:`Token ${token}`
                        }
                    });

                    if (response.status === 200) {
                        useStore().clearToken()
                        this.$router.push('/login');
                    } else {
                        console.error('Logout request failed:', response.statusText);
                    }
                } else{
                    console.error('Token not found')
                }
   
            } catch (error){
                console.log('Error ao fazer logout', error);
            }
            
        }
    }
}
</script>

<style scoped>
.user-options{
  background-color: #171416;
  position: absolute;
  width: 150px;
  right: 5vw;
  display: none;
}
.user-options button{
  z-index: 1;
  background-color: transparent; 
  width: 100%;
  font-size: 16px;
  color: white;

}
.user-options button:hover{
  background-color: #373536;
}
</style>