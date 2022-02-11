<template>
  <div v-if="resourceDetails">
    <div class="type-name">
      {{ resourceDetails.resource_type }}
      {{ resourceDetails.description }}
      <img :src="resourceDetails.picture" alt="image" />
    </div>
    <div class="card-container">
      <div
        class="resource-card"
        :key="resource_card.id"
        v-for="resource_card in resourceCardList"
      >
        <ResourceCard
          v-bind:resource_card="resource_card"
          @handleDelete="handleDelete"
          @resourceCardList="resourceCardList"
        />
      </div>
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
  font-size: 100px;
  justify-content: space-around;
  width: 100%;
  color: rgba(161, 255, 255, 0.568);
  max-height: 300px;
}

.card-container {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  grid-auto-rows: auto;
  grid-gap: 1rem;
}

.resource-card {
  margin: 30px;
  display: flex;
  flex-wrap: wrap;
  justify-content: space-evenly;
  background: rgba(29, 82, 110, 255);
  border-radius: 10px;
  text-transform: initial;
  padding: 20px;
}
</style>
