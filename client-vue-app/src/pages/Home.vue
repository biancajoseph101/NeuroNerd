<template>
  <div>
    <h1>sliding caurosel thing here</h1>
    <div v-for="tag in tag_array" :key="tag.id">
      <h2>{{ tag_array[0].category_name }}</h2>
      <img :src="tag_array[0].image_url" />
    </div>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'Home',
  components: {},
  data: () => ({
    tag_array: Array
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

img {
  max-height: 200px;
  border-radius: 7px 7px 0 0;
}
</style>
