<template>
  <div id="postform">
    <div class="form-container">
      <form @submit="handleSubmit">
        <div class="flex">
          <h2>Knowledge is power. Share with the community!</h2>

          <select
            name="resourceTypes"
            :value="resourceTypes"
            class="selectType"
            v-on:select="handleFormChange"
          >
            <option value="">Select Resource Type</option>
            <option value="resource_type">
              {{ resourceTypes[0].resource_type }}
            </option>
            <option value="resource_type">
              {{ resourceTypes[1].resource_type }}
            </option>
            <option value="resource_type">
              {{ resourceTypes[2].resource_type }}
            </option>
          </select>
          <input
            placeholder="Topic"
            :value="topic"
            name="topic"
            type="topic"
            v-on:input="handleFormChange"
          />
          <input
            placeholder="Link"
            :value="link"
            name="link"
            type="link"
            v-on:input="handleFormChange"
          />
          <input
            placeholder="Image URL"
            :value="image"
            name="image"
            type="text"
            v-on:input="handleFormChange"
          />
          <input
            placeholder="Content"
            :value="content"
            name="content"
            type="content"
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
  name: 'ResourceForm',
  data: () => ({
    resource_type: Object,
    topic: '',
    link: '',
    image: '',
    content: '',
    resourceTypes: ''
  }),
  mounted() {
    this.getResourceTypes();
  },
  methods: {
    async getResourceTypes() {
      const res = await axios.get(`http://localhost:8000/resourcetypes/`);
      this.resourceTypes = res.data;
    },

    handleFormChange(e) {
      this[e.target.name] = e.target.value;
    },
    async handleSubmit(e) {
      e.preventDefault();
      const res = await axios.post(
        `http://localhost:8000/resources/`,
        {
          topic: this.topic,
          link: this.link,
          image: this.image,
          content: this.content
        },
        {
          auth: {
            username: 'nerduser',
            password: 'nerdpassword'
          }
        }
      );
      this.$router.push(`/resources/${res.data.id}`);
      this.$router.go();
    }
  }
};
</script>

<style scoped>
.selectType {
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
