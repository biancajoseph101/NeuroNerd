<template>
  <div class="menu-item" @click="isOpen = !isOpen">
    <img :src="resourceDetails.picture" alt="" />
    <div class="center">{{ resourceDetails.resource_type }}</div>
    <div :key="resource_card.id" v-for="resource_card in resourceList">
      <ResourceCard
        v-bind:resource_card="resource_card"
        @handleDelete="handleDelete"
      />
    </div>
  </div>
</template>

<script>
// import { defineComponent } from '@vue/composition-api'
import axios from 'axios';
import ResourceCard from '../components/ResourceCard.vue';
export default {
  name: 'ResourceType',
  components: {
    ResourceCard
  },
  data: () => ({
    resourceDetails: null,
    resourceList: null
  }),
  mounted: function () {
    this.getResourceDetails();
  },
  methods: {
    async getResourceDetails() {
      let id = parseInt(this.$route.params.resource_id);
      const res = await axios.get(`http://localhost:8000/resources/${id}`);
      console.log(res.data);
      this.resourceDetails = res.data;
      this.resourceList = res.data.resource_list;
    },
    handleDelete(id) {
      this.resourceList = this.resourceList.filter(
        (resource) => resource.id !== id
      );
    }
  }
};
</script>
