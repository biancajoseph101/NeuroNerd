<template>
  <div v-if="resourceDetails">
    <div>{{ resourceDetails.resource_type }}</div>
    <div>{{ resourceDetails.description }}</div>

    <img :src="resourceDetails.picture" alt="image" />

    <div :key="resource_card.id" v-for="resource_card in resourceCardList">
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
    resourceCardList: null
  }),
  mounted: function () {
    this.getResourceDetails();
  },
  methods: {
    async getResourceDetails() {
      let id = parseInt(this.$route.params.resource_id);
      const res = await axios.get(`http://localhost:8000/resourcetypes/${id}`);
      //   console.log(res.data);
      this.resourceDetails = res.data;
      this.resourceCardList = res.data.resource_list;
    },
    handleDelete(id) {
      console.log(id);
      this.resourceCardList = this.resourceCardList.filter(
        (resourceCard) => resourceCard.id !== id
      );
    }
  }
};
</script>

<style scoped>
img {
  max-height: 200px;
  border-radius: 7px 7px 0 0;
}

.container {
  position: relative;
  display: flex;
  justify-content: center;
}

.center {
  position: absolute;
  top: 50%;
  text-align: center;
  font-size: 22px;
  color: black;
}

img {
  width: 100%;
  height: auto;
}

.blur {
  opacity: 0.6;
}
</style>
