<template>
  <div id="app">
    <Nav />
    <ResourceDrop />
    <router-view header="Header"></router-view>
  </div>
</template>

<script>
import Nav from './components/Nav.vue';
import ResourceDrop from './components/ResourceDrop.vue';
export default {
  name: 'App',
  components: {
    Nav,
    ResourceDrop
  }
};
</script>

<style>
#app {
  font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande',
    'Lucida Sans', Arial, sans-serif;
  text-transform: uppercase;

  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: rgba(73, 174, 173, 255);
  margin-top: 10px;
  background-color: rgba(7, 27, 54, 255);
  background-position: 100%;
}

body,
html {
  padding: 0;
  margin: 0;
  background-color: rgba(7, 27, 54, 255);

  width: 100%;
  min-height: 100%;
}
</style>
