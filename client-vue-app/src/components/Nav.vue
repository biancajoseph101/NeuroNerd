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
        Post</router-link
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
  max-height: 250px;
  margin-right: 20px;
  margin-left: 20px;
  margin-top: 50px;
  margin-bottom: 50px;
  border-radius: 20px;
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
  background-color: rgba(248, 248, 255, 0.336);
  margin-left: 50%;
}
nav {
  margin-top: 100px;
  font-size: 35px;
  display: flex;
  height: 250px;
  flex-direction: row;
  justify-content: flex-start;
  align-items: center;
  background-color: rgba(84, 2, 100, 0.541);
  /* background-color: #252e79; */
}
</style>
