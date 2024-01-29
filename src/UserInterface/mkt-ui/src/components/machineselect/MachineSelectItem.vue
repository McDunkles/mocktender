<template>
    <div class="item">
      <div class="machine-item" v-on:click="this.$router.push({path: '/menu'});">
        <h2>
          <slot name="heading"></slot>
        </h2>
      </div>
    </div>
  </template>

  <style scoped>
  
  .machine-item {
    margin-top: 2rem;
    flex: 1;
    text-align: center;
  }
  
  
  h2 {
    font-size: 2rem;
    font-weight: 500;
    margin-bottom: 0.4rem;
    color: var(--color-heading);
  }

  h2:hover {
    color: gray;
    /* border: 1px solid #000000 */
  }
  </style>
  