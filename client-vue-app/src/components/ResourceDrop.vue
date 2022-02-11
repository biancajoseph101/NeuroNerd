<template>
  <div class="menu-item" @click="isOpen = !isOpen">
    <a href="#">
      {{ title }}
    </a>
    <transition name="fade" apear>
      <div class="sub-menu" v-if="isOpen">
        <div class="mini-item" :key="resource.id" v-for="resource in resources">
          <div @click="selectResource(resource.id)">
            {{ resource.resource_type }}
          </div>
        </div>
        <div class="mini-item">
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
.mini-item:hover {
  font-weight: bolder;
  cursor: pointer;
}
.menu-item {
  display: block;
  color: white;
  text-decoration: none;
  font-size: 35px;
}

a {
  color: white;
  text-decoration: none;
  margin-top: 50px;
}
.sub-menu {
  display: block;
  margin-right: 8px;
  margin-top: 10px;
  text-transform: none;
  cursor: pointer;
  color: white;
  text-decoration: none;
  background-color: rgba(0, 0, 0, 0.411);
  border-radius: 15px;
  padding: 10px;
}
</style>
