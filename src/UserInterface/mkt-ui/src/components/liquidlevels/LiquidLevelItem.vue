<template>
    <div class="menu-option">

      <div class="level">

        <div class = "inner" :style="cssVars"></div>

        <h2 class="temp">

        </h2>
      </div>

      <h2 class="Label">
        {{liquid_info.liquid}}
        <slot name="heading"></slot>
      </h2>
      <h2>Capacity: {{liquid_info.liquidLevelPercentage}}%</h2>
  </div>
</template>


<script>
  import UrlUtils from "@/js/url-utils"
  import LiquidContainerMappingRepository from '../../js/liquid-container-mapping-repo'

  let liquidContainerMappingRepo = new LiquidContainerMappingRepository()

  export default {
    name: "LiquidLevelItem",
  
    props: {
      containerNo: Number,
      container_colour: String
    },
  
    data() {
      return {
        liquid_info: String
      }
    },
  
    created() {
      console.log("LiquidLevelItem Component Created");

      //this.getMocktales();

      console.log("containerNo = "+this.containerNo);

      this.getLiquidLevel();

      console.log("Test = "+this.liquid_info);

    },
  
    mounted() {
  
    },

    computed: {

      cssVars() {
        return {
          '--height': this.liquid_info.liquidLevelPercentage + '%',
          '--bottom': (0.3 * this.liquid_info.liquidLevelPercentage - 30) + 'rem'
        }
      }

    },
  
    methods: {
  
      async getLiquidLevel() {

        let searchParam = {
          containerNo: this.containerNo
        }

        let res = await liquidContainerMappingRepo.findByContainerNo(searchParam)
        .then( (response) => this.liquid_info = response ); 
      },

      onclick() {
        console.log("Ayo my containerNo is "+containerNo);
      }
  
    }
  }

</script>


<style scoped>
  
  .level {
    margin-top: 2rem;
    margin-left: 5rem;
    margin-right: 5rem;
    height: 30rem;
    width: 5rem;
    flex: 1;
    text-align: center;
    place-items: end;
    display: inline-block;
    border: 1px solid #000000;
  }

  .inner {
    height: var(--height);
    background-color: black;
    bottom: var(--bottom);
  }

  .menu-option {
    text-align: center;
    display: inline-block;
  }
  
  
  .temp {
    font-size: 2rem;
    font-weight: 500;
    margin-bottom: 0.4rem;
    color: var(--color-heading);
  }

  .temp:hover {
    color: gray;
    /* border: 1px solid #000000 */
  }
</style>
  