<template>
  <div id="app">
    <Nav />
    <router-view header="Header"></router-view>
  </div>
</template>

<script>
import Nav from './components/Nav.vue';
export default {
  name: 'App',
  components: {
    Nav
  }
};
</script>

<style>
#app {
  font-family: 'Courier New', Courier, monospace;

  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #ffffff;
  margin-top: 10px;
  background-color: rgba(153, 141, 221, 0.753);
  background-position: 100%;
}

body,
html {
  padding: 0;
  margin: 0;
  background-color: #252e79;

  width: 100%;
  min-height: 100%;
}
</style>
