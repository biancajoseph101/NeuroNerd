<template>
  <!-- <nav>
    <router-link to="/" name="Home" class="nav-btn">Home</router-link>
    <router-link to="/categoryform" class="nav-btn">Add a Category</router-link>
    <router-link to="/imageform" class="nav-btn">Upload a Picture</router-link>
  </nav> -->
  <h1>nav</h1>
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
