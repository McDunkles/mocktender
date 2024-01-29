<script setup lang="ts">
import LoginField from './LoginField.vue'
</script>

<template>
  <LoginField>
    <template #heading>Username</template>
  </LoginField>

  <LoginField>
    <template #heading>Password</template>
  </LoginField>

</template>