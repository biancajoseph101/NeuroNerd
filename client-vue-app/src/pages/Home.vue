<template>
  <div>
    <h1>home</h1>
    <div>
      <h2>{{ tag_array.category_name }}</h2>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'Home',
  components: {},
  data: () => ({
    tag_array: []
  }),
  mounted() {
    this.getTags();
  },
  methods: {
    async getTags() {
      const res = await axios.get(`http://localhost:8000/tags/`);
      this.tag_array = res.data;
      console.log(this.tag_array);
    }
    // handleDelete(id) {
    //   this.tag_aray = this.tag_array.filter((post) => post.id !== id);
    // }
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
