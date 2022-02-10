<template>
  <div>
    <h1>Articles</h1>
    <div class="container" v-for="tag in tag_array" :key="tag.id">
      <h2>{{ tag.title }}</h2>
      <h4>{{ tag.date }}</h4>
      <img :src="tag.image_url" />
      <h5>{{ tag.content }}</h5>

      <h5 class="source">
        source: <a href="#">{{ tag.source }}</a>
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
h3 {
  color: #80cbc4;
}

a {
  color: rgb(16, 7, 100);
}
.container {
  margin: 50px;
  display: flex;
  flex-wrap: wrap;
  flex-direction: row;
  justify-content: space-around;
  background: rgba(0, 0, 255, 0.342);
  border-radius: 10px;
}

img {
  max-height: 200px;
  border-radius: 7px 7px 0 0;
}
</style>
