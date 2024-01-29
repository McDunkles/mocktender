<script setup>
//import TheWelcome from '../components/TheWelcome.vue'
import { RouterView } from 'vue-router'
</script>


<template>
  <div class="content">

    <h2 class="welcome-message">Welcome Back, VueUser</h2>
    <img alt="Mocktender Thumbnail" class="logo" src="@/assets/mkt-thumbnail.png" width="750" height="250"/>
  
  </div>
</template>


<script>

  export default {
    name: "HomeView",

    props: {
      name: String
    },

    data() {
      return {
        username: String
      }
    },

    created() {

      //this.username = this.name;
      this.username = "User";

      console.log("HomeView Page Created, Username = "+this.username);
    },

    mounted() {

    },

    computed: {

    },

    methods: {
  
    }
  }

</script>


<style scoped>

.content {
  background-color: #DDDDDD;
  vertical-align: top;
  height: 100%;
  display: inline-block;
}

.welcome-message {
  text-align: center;
  margin-bottom: 2rem;
}

</style>
