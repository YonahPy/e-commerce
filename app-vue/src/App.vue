<template>
  <nav class="nav-header">
      <div class="main-categories" :class="{'is-active':menu}">
        <div class="drop-down-categories" @click="toggleDropdown('women')">
          <p >Women <img src="./assets/icons/down-arrow.png" alt="icon-down-arrow"></p>
          <div class="drop-down" v-show="activeDropdown === 'women'">
            <DropDown :categories="filterCategoriesWomen"></DropDown>
          </div>
        </div>
        <div class="drop-down-categories" @click="toggleDropdown('men')">
          <p >Men <img src="./assets/icons/down-arrow.png" alt="icon-down-arrow"></p>
          <div class="drop-down" v-show="activeDropdown === 'men'">
            <DropDown :categories="filterCategoriesMen"></DropDown>
          </div>
        </div>
        <div class="drop-down-categories" @click="toggleDropdown('kids')">
          <p>Kids <img src="./assets/icons/down-arrow.png" alt="icon-down-arrow"></p>
          <div class="drop-down" v-show="activeDropdown === 'kids'">
            <DropDown :categories="filterCategoriesKids"></DropDown>
          </div>
        </div>
      </div>
      <div class="home">
        <RouterLink to="/">Fashion</RouterLink>
      </div>
      
      <div class="controls">
      
          <div class="login">
            <Login v-if="!token" :width="'100%'" :height="'40px'">
            </Login>
          </div>
        <div>
          <div  class="searchbox" :class="{'searchbox-show': showSearch}">
            <button type="button" class="search-icon" @click="showSearch = !showSearch" :disabled="!token">
              <img src="./assets/icons/search.png" alt="search">
            </button>
            <input type="search" v-model="search" placeholder="Search" class="search-input" v-if="showSearch" @keydown.enter="handleSearch">
          </div>
        </div>
        <div class="div-user" :style="{'display': display}">
          <p class="button-user"><img src="./assets/icons/user.png" alt="user"></p>
      
          <div class="user-options" v-if="token">
              <UserOptions>
              </UserOptions>
          </div>
        </div>
        <div class="div-favorite" :style="{'display': display}">
          <RouterLink :to="{name: 'favorite'}" class="button-favorite"><img src="./assets/icons/love.png" alt="favorite"></RouterLink>
        </div>
        <div class="div-bag" :style="{'display': display}">
          <RouterLink :to="{name: 'myCart'}" class="button-bag"><img src="./assets/icons/shopping-bag.png" alt="shopping-bag"></RouterLink>
        </div>
    

      <div  class="toggle-label" @click="menu = !menu"  :class="{'is-active': menu}"
      :style="{'display': display}">
        <div class="toggle-button" id="toggle" ></div>
      </div>
    </div>


  </nav>
  <RouterView></RouterView>

  <footer>
    <div class="footer-socials">
      <p class="footer-brand">Fashion</p>
      <p>Online brand clothing store in 2013 in Home. Fashion focuses on seling only quality and branded item, limited edition collector by fashion designers</p>
      <div class="socials-icons">
        <img src="./assets/icons/facebook.png" alt="icon-facebook">
        <img src="./assets/icons/instagram.png" alt="icone-instagram">
        <img src="./assets/icons/twitter.png" alt="icone-twitter">
      </div>
    </div>

    <nav class="footer-nav">
      <div class="footer-main-categories">
        <h3>NAVIGATION</h3>
        <p @click="pushProducts('women')">WOMEN</p>
        <p @click="pushProducts('men')">MEN</p>
        <p @click="pushProducts('kids')">KIDS</p>
        <p>BRANDS</p>
      </div>

      <div>
        <h3>CUSTOMERS</h3>
        <p>PROMOTIONS</p>
        <p>DELIVERY</p>
        <p>PAYMENT</p>
        <p>GIFTCARD</p>
      </div>

      <div>
        <h3>ABOUT</h3>
        <p>NEWS</p>
        <p>PUBLIC OFFER</p>
        <p>USER AGREEMENT</p>
        <p>PRIVACY POLICY</p>
      </div>
    </nav>
  </footer>
</template>

<script>
import { RouterLink, RouterView } from 'vue-router'
import DropDown from './components/DropDown.vue'
import axios from 'axios'
import { useStore } from './stores/store'
import Login from './components/ButtonLogin.vue'
import UserOptions from './components/UserOptions.vue'

export default{
  data(){
    return{
      showSearch: false,
      listCategories: null,
      activeDropdown: null,
      search: '',
      menu: false,
      display: 'block'
    }
  },
  components:{
    DropDown,
    Login,
    UserOptions,
  },
  mounted(){
    this.getDataCategories()
  },
  computed:{
    filterCategoriesWomen(){
      if (this.listCategories){
        return this.listCategories.filter(function(category){
          return category.category_primary === 2
        })
      } else{
        return []
      }
    },
    filterCategoriesMen(){
      if (this.listCategories){
        return this.listCategories.filter(function(category){
          return category.category_primary === 3
        })
      } else{
        return []
      }
    },
    filterCategoriesKids(){
      if (this.listCategories){
        return this.listCategories.filter(function(category){
          return category.category_primary === 4
        })
      } else{
        return []
      }
    },
    token(){
      return useStore().token
    },

  },
  watch:{
    showSearch(newValue){
      if(newValue === true){
        this.display = 'none';
      } else{
        this.display = 'block';
      }
    }
  },
  methods:{
    getDataCategories(){
      axios.get('http://127.0.0.1:8000/api/sub-category/')
      .then(response => {
        this.listCategories = response.data.results;
      })
      .catch(error => {
        console.log('Erro ao buscar produtos', error)
      })
    },
    toggleDropdown(category) {
      this.activeDropdown = this.activeDropdown === category ? null : category;
    },
    pushProducts(category){
      this.$router.push('/products')
      if (category === 'women'){
        useStore().setCategory("Women's Clothing", 1)
      } else if (category === 'men'){
        useStore().setCategory("Men's Clothing", 13);
      } else{
        useStore().setCategory("Boys' kids Clothes", 24);
      }
    },
    handleSearch(){
      this.$router.push({name: 'search', params: {search: this.search}});
    } 
  },

  
}

</script>

<style >
*{
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  text-decoration: none;
  
}

:root{
  --primary-white :#fff5ee;
  --primary-orange: #e49e6c;

  --black:#171416;
  --dark-grey: #373536;
  --desatured-grey: #908d90;
  --light-grey: #d4cdd4;

  --blue:#219fff;
  --green: #17bd8d;
  --orange: #ffa114;
  --red: #ff4e3e;

}

h1,h2,h3,h4,h5{
  font-family: 'DM Serif Display', serif;
  color: var(--black);
}
p,a,span,div, button{
  font-family: 'Manrope', sans-serif;
  color: var(--black);
}
.nav-header{
  display: flex;
  justify-content: space-between;
  padding: 20px;
  align-items: center;

}

.controls{
  display: flex;
  align-items: center;
  margin-right: 20px;
}
.controls img{
  width: 100%;

}

.controls button, .div-user, .div-favorite, .div-bag{
  width: 25px;
  height: 25px;
  margin-right: 15px;
  border: none;
  background-color: transparent;
  cursor: pointer;
  
}
.login{
  margin-right: 12px;
  width: 100px;

}
.searchbox{
  display: flex;
  align-items: center;
  height: 40px;

}
.search-input{
  border: none;
  background-color: rgb(236, 230, 230);
  height: 45px;
  width: 300px;
  padding-left: 10px;
  border-radius: 20px;
  padding-right: 5px;
  
}
.search-input::placeholder{
  font-size: 17px;
}
.search-input:focus{
  outline: none;
  border: 1px solid #e49e6c;
}
.searchbox-show{
  margin-right: 10px;
  
}
.main-categories{
  margin-left: 20px;
  display: flex;
  position: relative;
}
.drop-down-categories{
  margin-inline: 5px;
}
.main-categories p{
  margin-left: 15px;
  font-size: 18px;
  cursor: pointer;
  
}
.main-categories p:hover{
  color: var(--primary-orange);
}
.main-categories p img{
  height: 8px;
  margin-left: 3px;
}
.drop-down{
  position: absolute;

}

.div-user:hover .user-options{
  display: block;
}


.home a{
  font-size: 25px;
}

.socials-icons img{
  border-radius: 50%;
  margin-left: 5px;
  cursor: pointer;
}

footer{
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
  margin-top: 30px;
}

.footer-socials{
  margin-left: 3vw;
  
}

.footer-brand{
  font-size: 25px;
}

.footer-socials p{
  margin-right: 100px;
  margin-block: 10px;
}

.footer-nav{
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
}
.footer-main-categories{
  display: flex;
  flex-direction: column;
  justify-content: center;
 
}
.footer-main-categories p:hover{
  color: var(--primary-orange);
  cursor: pointer;
}
.footer-nav h3{
  margin-bottom: 10px;
}

/*menu */*

.toggle-label {
  display: none;
  cursor: pointer;
}

.toggle-button {
  display: none;
  width: 30px;
  height: 3px;
  background-color: #333;
  position: relative;
  transition: transform 0.4s, opacity 0.4s;
  
}

.toggle-button::before,
.toggle-button::after {
  content: '';
  width: 30px;
  height: 3px;
  background-color: #333;
  position: absolute;
  transition: transform 0.4s, opacity 0.4s;
}

.toggle-button::before {
  top: -10px;
}

.toggle-button::after {
  top: 10px;
}

.toggle-label.is-active  .toggle-button::before {
  transform: translateY(10px) rotate(-0deg);
  background-color: white;
}

.toggle-label.is-active  .toggle-button::after {
  transform: translateY(-10px) rotate(-90deg);
  background-color: white;
}

.toggle-label.is-active  .toggle-button {
  transform: rotate(45deg);
  background-color: transparent;
}

@media screen and (max-width: 800px){
  footer{
    grid-template-columns: 1fr;
    gap: 60px;
    margin-bottom: 40px;
  }
  .footer-socials{
    padding-inline: 40px;
  }
}
@media screen and (max-width: 780px) {
  .toggle-label {
    display: block;
    
}
.toggle-button {
  display: block;
}
  .nav-header {
    position: relative;
  }
  .main-categories {
    display: none; 
  }
  .is-active.main-categories{
    display: flex;
    flex-direction: column;
    position: absolute;
    background-color: #171416;
    top: 0vh;
    right: 0;
    width: 50vw;
    height: 100vw;
    

  }
  
  .is-active.main-categories p{
    color: white;
    margin-top: 10px;
    padding-top:10px ;
  }

  .drop-down-categories {
    display: none;
  }

  .is-active .drop-down-categories {
    display: block;
  }

  .controls{
    width: 50%;
    display: flex;
    justify-content: space-eve;
    align-items: center;
  }
  .controls .div-user, .div-favorite, .div-bag{
    display: flex;
    align-items: center;
    margin-right: 35px;
    width: 7vw;

  }
  .searchbox .search-icon{
    display: flex;
    align-items: center;
    margin-right: 25px;
    width: 30px;
  }
  
  .home{
    margin-left: 40px;
  }
  .searchbox-show .search-input{
    width: 40vw;
    height: 50px;
  }
  .searchbox-show .search-input::placeholder{
    font-size: 16px;
  }
  .searchbox-show + .toggle-label {
    display: none;
  }
}
@media screen and (max-width: 675px){
  .footer-nav{
    flex-direction: column;
    justify-content: center;
    align-items: center;
    gap: 30px;
  }

  .controls{  
    width: 80vw;
  }
  .controls .div-user, .div-favorite, .div-bag{
    width: 30px;
  }
  
}

</style>
