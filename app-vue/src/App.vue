<template>
  <nav class="nav-header">
    <div class="main-categories">
      <RouterLink to="#">Women</RouterLink>
      <RouterLink to="#">Men</RouterLink>
      <RouterLink to="#">Kids</RouterLink>
    </div>

    <div class="home">
      <RouterLink to="#">Fashion</RouterLink>
    </div>

    <div class="controls">
      <form action="#" method="post">
        <div class="searchbox">
          <button class="search-icon">
            <img src="./assets/icons/search.png" alt="search">
          </button>
        </div>
      </form>

      <div class="div-user">
        <button class="button-user"><img src="./assets/icons/user.png" alt="user"></button>
      </div>

      <div class="div-favorite">
        <button class="button-favorite"><img src="./assets/icons/love.png" alt="favorite"></button>
      </div>

      <div class="div-bag">
        <button class="button-bag"><img src="./assets/icons/shopping-bag.png" alt="shopping-bag"></button>
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
        <RouterLink to="#">WOMEN</RouterLink>
        <RouterLink to="#">MEN</RouterLink>
        <RouterLink to="#">KIDS</RouterLink>
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
p,a,span,div{
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
.controls button{
  width: 25px;
  height: 25px;
  margin-right: 15px;
  border: none;
  background-color: transparent;
  cursor: pointer;

}
.main-categories{
  margin-left: 20px;
}
.main-categories a{
  margin-left: 15px;
  font-size: 18px;
}
.main-categories a:hover{
  color: var(--primary-orange);
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
}
.footer-main-categories a:hover{
  color: var(--primary-orange);
  cursor: pointer;
}
.footer-nav h3{
  margin-bottom: 10px;
}
</style>
