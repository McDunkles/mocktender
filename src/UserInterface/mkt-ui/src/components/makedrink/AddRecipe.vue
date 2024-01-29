<script setup>

</script>

<template>
<h2 class="title">Add A Recipe</h2>

<div class = "div-input">
    <label label="MocktailName">Mocktail Name </label>
    <input v-model="mkt_name"/>
</div>

<h4 class="step-label">Step 1</h4>

<div class = div-input>
    <label label="liquid1">Drink </label>
    <input v-model="liquid1">

    <label label="amount1">Amount (mL) </label>
    <input v-model="amount1">
</div>

<h4 class="step-label">Step 2</h4>

<div class = div-input>
    <label label="liquid2">Drink </label>
    <input v-model="liquid2">

    <label label="amount2">Amount (mL) </label>
    <input v-model="amount2">
</div>

<h4 class="step-label">Step 3</h4>

<div class = div-input>
    <label label="liquid3">Drink </label>
    <input v-model="liquid3">

    <label label="amount3">Amount (mL) </label>
    <input v-model="amount3">
</div>

<div class = div-input>
    <button class="save-button" v-on:click="this.add_recipe();">Add Recipe</button>
</div>

</template>

<script>

  import UrlUtils from "../../js/url-utils"
  import MocktailRecipeRepository from "../../js/mocktail-recipe-repo"

  export default {
    name: "AddRecipe",
  
    props: {
    },
  
    data() {
      return {
        mkt_name: '',
        liquid1: '',
        amount1: '',
        liquid2: '',
        amount2: '',
        liquid3: '',
        amount3: ''
      }
    },
  
    created() {
      console.log("AddRecipe Component Created");


    },
  
    mounted() {
  
    },

    computed: {
        
    },
  
    methods: {
  
        get_request_params() {

            let params = {
                name: this.mkt_name,
                liquid1: this.liquid1,
                amount1: this.amount1,
                liquid2: this.liquid2,
                amount2: this.amount2,
                liquid3: this.liquid3,
                amount3: this.amount3
            };

            return params;
        },

        to_url_format() {

            let params = {
                name: this.mkt_name,
                liquid1: this.liquid1,
                amount1: this.amount1,
                liquid2: this.liquid2,
                amount2: this.amount2,
                liquid3: this.liquid3,
                amount3: this.amount3
            };

            return UrlUtils.toUrlEncoded(params);

        },

        async add_recipe_async() {

            console.log("URL FORMAT = "+this.to_url_format());

            let params = this.get_request_params();

            let mocktailRecipeRepo = new MocktailRecipeRepository();

            let mkt_resp = await mocktailRecipeRepo.addMocktail(params)
            .then( (response) => console.log("Response = "+JSON.stringify(response)) );

        },

        add_recipe() {
            this.add_recipe_async();

            this.$router.push("/make");
        }
    }
  }

</script>

<style scoped>
h2 {

    margin-top: 2rem;
    flex: 1;
    text-align: center;
  
    font-size: 2.5rem;
    font-weight: 600;
    margin-bottom: 0.4rem;
    color: var(--color-heading);
  }

.title {
    margin-bottom: 2rem;
}

.div-input {
    margin-top: 0.25rem;
    align-content: center;
    text-align: center;
}

.step-label {
    margin-top: 1rem;
}

label {
    margin-right: 0.5rem;
}

input {
    margin-right: 3rem;
}

.save-button {
    margin-top: 2rem;
}

</style>

<style scoped>

.title-div {
  text-align: center;
  background-color: #CCCCCC;
}

.title-text {
  font-size: 3rem;
  font-weight: 600;
  margin-bottom: 0.4rem;
  color: var(--color-heading);
}

</style>