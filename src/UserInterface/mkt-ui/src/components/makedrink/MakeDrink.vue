<script setup>
import MakeDrinkItem from './MakeDrinkItem.vue'
</script>

<template>

  <h3 class="modify" v-on:click="this.add_recipe();">Add Recipes</h3>

  <div class="top">
    <h2 class="title">Saved Recipes</h2>
  </div>

  <div v-for="elem in mocktail_recipe">
    <!-- <h2 class = "saved_mocktail">{{elem.name}}</h2> -->
    <MakeDrinkItem :mocktail_name=elem.name v-on:click="this.on_click(elem);">
      <template #heading>{{elem.name}}</template>
    </MakeDrinkItem>
  </div>

  <div class="brew-button-div">
    <button class="brew-button" v-on:click="this.brew_recipe();">Dispense</button>
  </div>

</template>


<script>
  import MocktailRecipeRepository from '../../js/mocktail-recipe-repo'
  import FirebaseRepository from '../../js/firebase-repo';

  let mocktailRecipeRepo = new MocktailRecipeRepository()
  let firebaseRepo = new FirebaseRepository()

  export default {
    name: "MakeDrink",

    props: {
      mocktail_name: String
    },

    data() {
      return {
        mocktail_recipe: String,
        test_mocktail: String,
        selected_mocktail: Object
      }
    },

    created() {
      console.log("MakeDrink Component Created");

      this.getMocktails();

    },

    mounted() {

    },

    computed: {

    },

    methods: {
  
      async getMocktails() {

        let res = await mocktailRecipeRepo.findAll()
        .then( (response) => this.mocktail_recipe = response ); 
      },


      async getMocktail(params) {


        let res = await mocktailRecipeRepo.find(params)
        .then( (response) => this.test_mocktail = response ); 
      },

      add_recipe() {
        console.log("Add my recipe!");

        let newPath = "/make/addRecipe"
        this.$router.push({path: newPath});
      },

      on_click(mock) {
        console.log("Been clicked!");

        //let my_var = JSON.stringify(this);
        //console.log("Test: "+my_var);

        //console.log("Name = "+mock_name);

        this.selected_mocktail = mock;

        console.log(JSON.stringify(mock));

      },

      brew_recipe() {
        console.log("[end-to-end] Stuff");

        console.log(JSON.stringify(this.selected_mocktail));

        firebaseRepo.sendRecipe(this.selected_mocktail);

        //firebaseRepo.sendMocktail
      }
  
    }
  }

</script>


<style scoped>

.top {
  text-align: center;
}

h2 {

  margin-top: 2rem;
  flex: 1;
  text-align: center;

  font-size: 2.5rem;
  font-weight: 600;
  margin-bottom: 0.4rem;
  color: var(--color-heading);
}


h3 {
  width: 100%;
  display: inline-block;
  text-align: end;
}

.saved_mocktail:hover {
  color: gray;
}

.title {
  background-color: #CCCCCC;
}

.brew-button-div {
  margin-top: 5rem;
  text-align: center;
}

.brew-button {
  width: 150px;
  height: 60px;
}

.brew-button:hover {
  background-color: #A9A9A9;
}
  
</style>