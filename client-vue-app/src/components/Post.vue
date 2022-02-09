<template>
  <div id="postform">
    <div class="form-container">
      <form @submit="handleSubmit">
        <div class="flex">
          <h5>Post</h5>
          <!-- <input
            placeholder="Category"
            :value="category"
            name="category"
            type="category"
            v-on:input="handleFormChange"
          /> -->
          <select
            name="category"
            :value="category"
            class="selectCat"
            v-on:select="handleFormChange"
          >
            <option value="">Select Category</option>
            <option value="category">{{ tags[0].category_name }}</option>
            <option value="category">{{ tags[1].category_name }}</option>
            <option value="category">{{ tags[2].category_name }}</option>
          </select>
          <input
            placeholder="Title"
            :value="title"
            name="title"
            type="title"
            v-on:input="handleFormChange"
          />
          <input
            placeholder="Content"
            :value="content"
            name="content"
            type="content"
            v-on:input="handleFormChange"
          />
          <input
            placeholder="ImageURL"
            :value="image_url"
            name="image_url"
            type="image_url"
            v-on:input="handleFormChange"
          />
          <input
            placeholder="Source"
            :value="source"
            name="source"
            type="source"
            v-on:input="handleFormChange"
          />
          <input
            placeholder="Author"
            :value="author"
            name="author"
            type="author"
            v-on:input="handleFormChange"
          />
          <button class="btn" type="submit">Submit Post</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'Post',
  data: () => ({
    category: Object,
    title: '',
    content: '',
    image_url: '',
    source: '',
    author: '',
    tags: ''
  }),
  mounted() {
    this.getTags();
  },
  methods: {
    async getTags() {
      const res = await axios.get(`http://localhost:8000/tags/`);
      this.tags = res.data;
    },

    handleFormChange(e) {
      this[e.target.name] = e.target.value;
    },
    async handleSubmit(e) {
      e.preventDefault();
      const res = await axios.post(
        `http://localhost:8000/posts/`,
        {
          title: this.title,
          content: this.content,
          image_url: this.image_url,
          source: this.source
        },
        {
          auth: {
            username: 'neuro',
            password: 'neuro'
          }
        }
      );
      this.$router.push(`/posts/${res.data.id}`);
      this.$router.go();
    }
  }
};
</script>

<style scoped>
.selectCat {
  min-width: 500px;
}
h3 {
  color: #80cbc4;
}
input {
  width: 500px;
  height: 60px;
  margin: 10px;
}
.flex {
  width: 100vw;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.btn {
  width: 509px;
  margin: 10px;
}
</style>
