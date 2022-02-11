<template>
  <nav>
    <div class="menu-item">
      <router-link to="/" name="Home" class="nav-btn"
        ><img class="logo" src="https://i.imgur.com/Ihwcu0y.jpg"
      /></router-link>
    </div>
    <div class="menu-item">
      <router-link to="/login" name="Login" class="nav-btn"
        >Login•
      </router-link>
    </div>
    <div class="menu-item">
      <router-link to="/news" name="news" class="nav-btn"> News• </router-link>
    </div>
    <div class="menu-item">
      <router-link to="/articles" name="articles" class="nav-btn">
        Articles•
      </router-link>
    </div>
    <div class="menu-item">
      <router-link to="/createpost" name="post" class="nav-btn">
        Post Article</router-link
      >
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
.logo {
  max-height: 80px;
  margin-right: 20px;
  margin-left: 20px;
}
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
  margin-left: 50%;
}
nav {
  font-size: 25px;
  /* position: absolute; */
  display: flex;
  flex-direction: row;
  justify-content: flex-start;
  align-items: center;
  background-color: #252e79;
}
</style>
