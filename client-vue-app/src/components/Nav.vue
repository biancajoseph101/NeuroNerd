<template>
  <nav>
    <router-link to="/" name="Home" class="nav-btn">Home</router-link>
  </nav>
</template>

<script>
export default {
  name: 'Nav',
  data: () => ({
    categories: null
  })
};
</script>

<style scoped>
.nav-btn {
  cursor: pointer;
  text-decoration: none;
  color: grey;
}
.nav-btn:hover {
  color: white;
  font-weight: bolder;
}
.nav-btn {
  color: white;
}
nav {
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  align-items: center;
  background-color: #80cbc4;
}
</style>
