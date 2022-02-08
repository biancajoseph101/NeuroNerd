<template>
  <div>
    <h1>home</h1>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'Home',
  components: {},
  data: () => ({
    post_array: []
  }),
  mounted() {
    this.getPosts();
  },
  methods: {
    async getPosts() {
      const res = await axios.get(`http://localhost:8000/posts/`);
      this.post_array = res.data;
    },
    handleDelete(id) {
      this.post_array = this.post_array.filter((post) => post.id !== id);
    }
  }
};
</script>
<style scoped>
h3 {
  color: #80cbc4;
}

.image-container-grid {
  display: flex;
  flex-wrap: wrap;
  flex-direction: row;
  justify-content: space-around;
}
</style>
