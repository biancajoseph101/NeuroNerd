<template>
  <div class="menu-item" @click="isOpen = !isOpen">
    <a href="#">
      {{ title }}
    </a>
    <transition name="fade" apear>
      <div class="sub-menu" v-if="isOpen">
        <div class="menu-item">
          <router-link to="/resources/{resource.id}">Mental Health</router-link>
        </div>
        <div class="menu-item">
          <router-link to="/resources/">Podcasts</router-link>
        </div>
        <div class="menu-item">
          <router-link to="/resources/{resource.id}">Research</router-link>
        </div>
      </div>
    </transition>
  </div>
</template>

<script>
export default {
  name: 'ResourceDrop',
  componenets: {},
  props: ['title'],
  data() {
    return {
      isOpen: false
    };
  }
};
</script>

<style>
.menu-item {
  color: white;
  text-decoration: white;
}
.sub-menu {
  color: white;
  text-decoration: none;
}
</style>
