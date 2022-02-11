<template>
  <!-- <nav>
    <div class="menu-item">
      <router-link to="/" name="Home" class="nav-btn"
        ><img class="logo" src="https://i.imgur.com/Ihwcu0y.jpg"
      /></router-link>
    </div>
    <div class="menu">
      <div class="menu-item">
        <router-link to="/login" name="Login" class="nav-btn"
          >Login•
        </router-link>
      </div>
      <div class="menu-item">
        <router-link to="/news" name="news" class="nav-btn">
          News•
        </router-link>
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
        <ResourceDrop title="☰" />
      </div>
    </div>
  </nav> -->

  <div class="nav">
    <div class="left">
      <router-link to="/" name="Home" class="nav-btn"
        ><img class="logo" src="https://i.imgur.com/QxQny93.png"
      /></router-link>
    </div>
    <div class="middle">
      <div class="item">
        <router-link to="/login" name="Login" class="nav-btn"
          ><img
            class="login"
            src="http://cdn.onlinewebfonts.com/svg/img_150170.png"
          />
        </router-link>
      </div>
      <div class="item">
        <router-link to="/news" name="news" class="nav-btn">
          News•
        </router-link>
      </div>
      <div class="item">
        <router-link to="/articles" name="articles" class="nav-btn">
          Articles•
        </router-link>
      </div>
      <div class="item">
        <router-link to="/createpost" name="post" class="nav-btn">
          Post</router-link
        >
      </div>
    </div>
    <div class="right">
      <ResourceDrop title="☰" />
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
  padding: 15px;
  display: inline-block;
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
  max-width: 500px;
}
.middle {
  text-align: left;
}
.right {
  max-width: 300px;
  text-align: right;
  font-size: 55px;
  margin-right: 15px;
}

.logo {
  max-width: 200px;
  margin: 5px;
  border-radius: 50%;
}
.logo:hover,
.login:hover {
  transform: translateX(20px) translateY(-3px);
}
.login {
  max-height: 100px;
  margin-left: 150px;
}
.item:hover {
  font-weight: bolder;
}

.resource-drop {
  z-index: 10;
}
</style>
