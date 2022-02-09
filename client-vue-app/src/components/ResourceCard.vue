<template>
  <div class="resource-container">
    <div class="container">
      <img :src="resource_card.image" alt="picture" />
      <div>
        {{ resource_card.topic }}
        {{ resource_card.link }}
      </div>
      <div>{{ resource_card.content }}</div>
      <div @click="deleteResource" class="deleteBtn">x</div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'ResourceCard',
  data: () => ({}),
  props: {
    resource_card: Object
  },
  methods: {
    async deleteResource() {
      await axios.delete(
        `http://localhost:8000/resources/${this.resource_card.id}`,
        {
          auth: {
            email: 'nerd@nerd.nerd',
            password: 'nerdpassword'
          }
        }
      );
      this.$emit('handleDelete', this.resource_card.id);
    }
  }
};
</script>

<style scoped>
img {
  max-height: 200px;
  margin: 20px;
}

.container {
  display: flex;
  align-items: center;
  margin: 20px;
}

.deleteBtn {
  width: 50px;
  height: 30px;
  background-color: #80cbc4;
  font-size: 20px;
  font-weight: 700;
  cursor: pointer;
  border-radius: 4px;
}

.deleteBtn:hover {
  background-color: #682424;
  color: white;
}
</style>
