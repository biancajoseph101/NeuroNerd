<template>
  <div v-if="resourceDetails">
    <div class="type-name">{{ resourceDetails.resource_type }}</div>
    <div>{{ resourceDetails.description }}</div>

    <img :src="resourceDetails.picture" alt="image" />
    <div :key="resource_card.id" v-for="resource_card in resourceCardList">
      <ResourceCard
        v-bind:resource_card="resource_card"
        @handleDelete="handleDelete"
        @resourceCardList="resourceCardList"
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
      // console.log(res.data.resource_list[i].resource_type);
      this.resourceDetails = res.data;
      this.resourceCardList = res.data.resource_list;
    },
    handleDelete(id) {
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
  border-radius: 4px;
}

/* .type-name {
  font-size: 75px;
  display: flex;
  justify-content: center;
} */
.type-name {
  margin-top: 50px;
  padding-top: 5px;
  display: flex;
  font-size: 60px;
  justify-content: space-around;
  width: 100%;
  color: #94eee58c;
}

.container {
  position: absolute;
  display: flex;
  align-items: center;
}
</style>
