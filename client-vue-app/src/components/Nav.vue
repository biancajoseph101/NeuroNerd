<template>
  <nav>
    <div class="menu-item">
      <router-link to="/" name="Home" class="nav-btn">Home</router-link>
    </div>
    <div class="menu-item">
      <router-link to="/createpost" name="post" class="nav-btn"
        >Add Article</router-link
      >
    </div>
    <div class="menu-item">
      <router-link to="/news" name="news" class="nav-btn">News</router-link>
    </div>
    <div class="menu-item">
      <router-link to="/login" name="Login" class="nav-btn">Login</router-link>
    </div>
    <div class="resource-drop">
      <ResourceDrop title="Resources ⇣" />
    </div>
  </nav>
</template>

<script>
import ResourceDrop from './ResourceDrop.vue';
export default {
  name: 'Nav',
  components: {
    ResourceDrop
  },
  data: () => ({
    resources: null
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

.resource-drop {
  margin-left: 10%;
  color: pink;
  text-decoration: hotpink;
}
nav {
  font-size: 25px;
  /* position: absolute; */
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  align-items: center;
  background-color: #000000;
}
</style>
