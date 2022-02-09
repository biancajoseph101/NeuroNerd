<template>
  <div class="resource-container">
    <div class="container">
      <img :src="resource_card.image" alt="picture" />
      <div>
        {{ resource_card.topic }}
        {{ resource_card.link }}
      </div>
      <div>{{ resource_card.content }}</div>
    </div>
    <div @click="deleteResource" class="deleteBtn">x</div>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'ResourceCard',
  data: () => ({
    showName: false,
    picclass: 'normal'
  }),
  props: {
    resource_card: Object
  },
  methods: {
    async deleteResource() {
      await axios.delete(
        `http://localhost:8000/resources/${this.resource_card.id}`,
        {
          auth: {
            username: 'nerduser',
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
  border-radius: 7px 7px 0 0;
}

.container {
  display: flex;
  justify-content: center;
}

.deleteBtn {
  width: 100%;
  background-color: #80cbc4;
  font-size: 20px;
  font-weight: 700;
  cursor: pointer;
  border-radius: 0 0 7px 7px;
}

.deleteBtn:hover {
  background-color: #682424;
  color: white;
}
</style>
