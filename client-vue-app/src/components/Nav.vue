<template>
  <nav>
    <div class="menu-item">
      <router-link to="/" name="Home" class="nav-btn">Home</router-link>
    </div>
    <div class="menu-item">
      <router-link to="/createpost" name="post" class="nav-btn"
        >Add Post</router-link
      >
    </div>
    <div class="menu-item">
      <router-link to="/news" name="news" class="nav-btn">News</router-link>
    </div>
    <div class="menu-item">
      <router-link to="/login" name="Login" class="nav-btn">Login</router-link>
    </div>
    <ResourceType title="ResourceType" />
  </nav>
</template>

<script>
export default {
  name: 'Nav',
  components: {
    ResourceType
  },
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
