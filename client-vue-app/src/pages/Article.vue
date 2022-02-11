<template>
  <div>
    <h1>Articles</h1>
    <div class="container" v-for="tag in tag_array" :key="tag.id">
      <h1>{{ tag.title }}</h1>

      <img :src="tag.image_url" />
      <h3>{{ tag.content }}</h3>

      <h5 class="source">
        <h4>{{ tag.date }}</h4>

        SOURCE: <a href="#">{{ tag.source }}</a>
      </h5>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'Article',
  components: {},
  data: () => ({
    tag_array: Array
  }),
  mounted() {
    this.getTags();
  },
  methods: {
    async getTags() {
      const res = await axios.get(`http://localhost:8000/posts/`);
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
a {
  color: rgb(16, 7, 100);
}
.container {
  margin: 50px;
  display: flex;
  flex-wrap: wrap;
  flex-direction: row;
  justify-content: space-around;
  background: rgba(29, 82, 110, 255);
  border-radius: 10px;
  text-transform: initial;
  padding: 25px;
}

img {
  max-height: 200px;
  border-radius: 10px;
}
</style>
