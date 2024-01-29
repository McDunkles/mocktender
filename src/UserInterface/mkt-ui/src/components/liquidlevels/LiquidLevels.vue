<script setup lang="ts">
import MenuOptionItem from './LiquidLevelItem.vue'
</script>

<template>

<div class="title-div">

<h2 class="title-text">Liquid Levels</h2>

</div>

  <div class="containers">
    <MenuOptionItem :containerNo=1 :container_colour="'Red'">
      <template #heading></template>
    </MenuOptionItem>

    <MenuOptionItem :containerNo=2 :container_colour="'Blue'">
      <template #heading></template>
    </MenuOptionItem>

    <MenuOptionItem :containerNo=3 :container_colour="'Green'">
      <template #heading></template>
    </MenuOptionItem>

</div>
  <!--
  <MenuOptionItem>
    <template #heading>(Container 2)</template>
  </MenuOptionItem>

  <MenuOptionItem>
    <template #heading>(Container 3)</template>
  </MenuOptionItem>
-->
</template>

<style scoped>

.containers {

  flex-wrap: wrap;
  align-self: center;
  align-items: center;
  text-align: center;

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