<script setup lang="ts">
import MenuOptionItem from './SettingItem.vue'
</script>

<template>

<div class="title-div">

  <h2 class="title-text">Settings</h2>

</div>

  <MenuOptionItem>
    <template #heading>View/Edit Saved Recipes</template>
  </MenuOptionItem>

  <MenuOptionItem>
    <template #heading>View/Edit Stored Liquids</template>
  </MenuOptionItem>

  <MenuOptionItem>
    <template #heading>Account Info</template>
  </MenuOptionItem>

  <MenuOptionItem>
    <template #heading>System Info</template>
  </MenuOptionItem>
</template>

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