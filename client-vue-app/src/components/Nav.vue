<template>
  <div class="nav">
    <div class="left">
      <router-link to="/" name="Home"
        ><img class="logo" src="https://i.imgur.com/QxQny93.png"
      /></router-link>
    </div>
    <div class="middle">
      <div class="item">
        <router-link to="/login" name="Login"> Login • </router-link>
      </div>
      <div class="item">
        <router-link to="/news" name="news" class="item">
          • Latest NeuroNews •
        </router-link>
      </div>
      <div class="item">
        <router-link to="/articles" name="articles"> • Community •</router-link>
      </div>
      <div class="item">
        <router-link to="/about" name="about"> • About </router-link>
      </div>
      <!-- <div class="item">
        <router-link to="/createpost" name="post" class="nav-btn">
          Post</router-link
        >
      </div> -->
    </div>
    <div class="right">
      <ResourceDrop class="hamburger" title="☰" />
    </div>
  </div>
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

<style>
.nav {
  display: flex;
  min-height: 100px;
  position: relative;
  z-index: 100;
  background-color: rgba(29, 82, 110, 255);
}
.item {
  font-size: 30px;
  display: inline-block;
  max-height: 60px;
}
.left,
.middle,
.right {
  height: 170px;
  min-width: 50px;
  flex: 1;
}
.left {
  text-align: left;
  max-width: 300px;
}
.middle {
  text-align: left;
  padding-bottom: 20px;
}
.right {
  max-width: 300px;
  text-align: right;
  margin-right: 15px;
}
.hamburger {
  font-size: 45px;
}
.logo {
  max-width: 200px;
  margin: 5px;
  border-radius: 50%;
}
.logo:hover {
  /* transform: translateX(20px) translateY(-3px); */
  filter: brightness(140%);
  transform: rotate(360deg);
  transition: all 0.9s ease-in-out;
}
.login {
  max-height: 50px;
  margin-left: 150px;
  margin-right: 20px;
  padding-top: 20px;
}
.item:hover {
  font-weight: bolder;
}

.resource-drop {
  z-index: 10;
}
</style>
