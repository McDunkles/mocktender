<template>


  <body class="body">

    <div class="topbar">

      <div class="machine"><h2>Machine: [name]</h2></div>

      <div class="account"><h2 class="accountinnertext">Account</h2></div>
<!--
      <div class="topbar-element"><h2>Top</h2></div> -->
    </div>

    <div class="mainpage">

    <div class="wrapper">
      <div class="sidebar">

        <h2>Menu</h2>

        <ul>

          <li><RouterLink to="/">Account</RouterLink></li>
          <!--<li><RouterLink to="/machineSelect">Machine Select</RouterLink></li>-->
          <!-- <li><RouterLink to="/menu">Main Menu</RouterLink></li> -->
          <li><RouterLink to="/make">Mocktail Recipes</RouterLink></li>
          <!-- <li><RouterLink to="/make/addRecipe">Add Recipe</RouterLink></li> -->
          <li><RouterLink to="/viewLiquidLevels">Current Liquid Levels</RouterLink></li>
          <li><RouterLink to="/settings">Settings</RouterLink></li>
          <li><RouterLink to="/adminSettings">Admin Settings</RouterLink></li>

        </ul>

      </div>
    </div>

    <RouterView class="curr-menu"/>

    </div>


  </body>
  <!-- <RouterView class="curr-menu"/> -->

</template>


<script setup>
import { RouterLink, RouterView } from 'vue-router'
import HomeView from './views/HomeView.vue'
</script>


<style scoped>

ul {
  list-style: none;
  box-sizing: border-box;
  text-decoration: none;
  margin: 0;
  padding: 0;
}

.wrapper {
    display: inline-block;
    width: 250px;
    height: 100%;
    position: relative;
    background-color: #B9B9B9;
    text-align: center;
  }

ul a.router-link-exact-active {
  color: #000000;
  text-decoration: underline;
}

li {
  margin-top: 1.5rem;
}

.body {
  place-content: top;
  background-color: #F1F1F1;
  align-items: start;
  display: block;

}

.topbar {
  width: 1000px;
  height: 50px;
  background-color: #E1E1E1;
  
}

.machine {
  width: 40%;
  display: inline-block;
  margin-left: 2rem;
}

.account {
  width: 50%;
  display: inline-block;
}

.accountinnertext {
  text-align: end;
  margin-right: 2rem;
}


.mainpage {
  height: 850px;
}

</style>
