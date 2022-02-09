<template>
  <div class="menu-item" @click="isOpen = !isOpen">
    <a href="#">
      {{ title }}
    </a>
    <transition name="fade" apear>
      <div class="sub-menu" v-if="isOpen">
        <div class="menu-item" :key="resource.id" v-for="resource in resources">
          <div @click="selectResource(resource.id)">
            {{ resource.resource_type }}
          </div>
        </div>
        <div class="menu-item">
          <router-link to="/createresource">Add Resource +</router-link>
        </div>
      </div>
    </transition>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'ResourceDrop',
  componenets: {},
  props: ['title'],
  data() {
    return {
      resources: null,
      isOpen: false
    };
  },
  mounted: function () {
    this.getResources();
  },
  methods: {
    async getResources() {
      const res = await axios.get(`http://localhost:8000/resourcetypes/`);
      this.resources = res.data;
    },
    selectResource(id) {
      this.$router.push(`/resources/${id}`);
      this.$router.go();
    }
  }
};
</script>

<style>
.menu-item:hover {
  font-weight: bolder;
  cursor: pointer;
}
.menu-item {
  color: white;
  text-decoration: none;
}
a {
  color: white;
  text-decoration: none;
}
.sub-menu {
  text-transform: none;
  cursor: pointer;

  color: white;
  text-decoration: none;
}
</style>
