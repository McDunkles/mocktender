<script setup lang="ts">
import MenuOptionItem from './MachineSelectItem.vue'
</script>

<template>

  <h2>
    Machine Select
  </h2>

 <!-- Routes to main menu -->
  <MenuOptionItem>
    <template #heading>Real</template>
  </MenuOptionItem>

  <!-- Routes to main menu -->
  <MenuOptionItem>
    <template #heading>Virtual</template>
  </MenuOptionItem>
</template>


<style scoped>

h2 {

  margin-top: 2rem;
  flex: 1;
  text-align: center;

  font-size: 2rem;
  font-weight: 500;
  margin-bottom: 0.4rem;
  color: var(--color-heading);
}

</style>