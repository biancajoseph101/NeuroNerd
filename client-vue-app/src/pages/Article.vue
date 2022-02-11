<template>
  <div>
    <h2>Articles</h2>
    <div class="container">
      <div class="article" v-for="tag in tag_array" :key="tag.id">
        <h4>{{ tag.date }}</h4>
        <h1>{{ tag.title }}</h1>

        <img :src="tag.image_url" />

        <div :class="{ readLess: readMore == true }" class="content">
          <h3>{{ tag.content }}</h3>
        </div>
        <div v-if="readMore == true" class="read-more">
          <button @click="readMore = !readMore">Expand</button>
        </div>
        <div v-else class="read-less">
          <button @click="readMore = !readMore">Collapse</button>
        </div>

        <h5 class="source">
          SOURCE: <a href="#">{{ tag.source }}</a>
        </h5>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'Article',
  components: {},
  data: () => ({
    tag_array: Array,
    readMore: false
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
  color: rgb(55, 43, 160);
}

button {
  background-color: white;
}
.article {
  margin: 50px;
  display: flex;
  flex-wrap: wrap;
  flex-direction: row;
  justify-content: space-around;
  background: rgba(29, 82, 110, 255);
  border-radius: 10px;
  text-transform: initial;
  padding: 2px;
  max-width: 800px;
}

.readLess {
  height: 200px;
  overflow: hidden;
}

.read-more,
.read-less {
  display: inline-block;
  color: white;
}
.container {
  /* max-width: 900px; */
  display: flex;
  justify-content: space-between;

  flex-direction: row;
}
img {
  height: 100px;
  border-radius: 3px;
  opacity: 80%;
}

h2 {
  margin-top: 50px;
  padding-top: 5px;
  display: flex;
  font-size: 60px;
  justify-content: space-around;
  width: 100%;
  color: #94eee58c;
}
</style>
