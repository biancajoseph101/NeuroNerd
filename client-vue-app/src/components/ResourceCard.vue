<template>
  <div class="resource-container">
    <div class="container">
      <h1>
        {{ resource_card.topic }}
      </h1>
      <img :src="resource_card.image" alt="picture" />
      <h2>
        <div>{{ resource_card.content }}</div>
      </h2>
      <h3 class="source">
        SOURCE: <a href="#">{{ resource_card.link }} </a>
      </h3>
    </div>
    <div class="showForm">
      <button @click="showForm = !showForm" class="updateBtn">edit</button>
      <div v-if="showForm" class="form-container">
        <form>
          <input
            placeholder="Edit topic"
            :value="newTopic"
            name="newTopic"
            type="text"
            v-on:input="handleFormChange"
          />
          <button @click="deleteResource" class="deleteBtn">x</button>

          <button @click="updateResource" class="submitBtn">submit</button>
        </form>
      </div>
      <div v-else></div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'ResourceCard',
  data: () => ({
    showForm: false,
    topic: '',
    newTopic: ''
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
            email: 'nerd@nerd.nerd',
            password: 'nerdpassword'
          }
        }
      );
      this.$emit('handleDelete', this.resource_card.id);
    },
    handleFormChange(e) {
      this[e.target.name] = e.target.value;
      this.newTopic = e.target.value;
      //   console.log(resource_type);
      //   console.log(this.newTopic);
    },

    async updateResource(e) {
      e.preventDefault();
      const response = await axios.get(
        `http://localhost:8000/resources/${this.resource_card.id}`
      );
      const list = response.data.resource_type;
      console.log(list);

      const res = await axios.put(
        `http://localhost:8000/resources/${this.resource_card.id}`,
        {
          showForm: true,
          topic: this.newTopic,
          resource_type: list
        },
        {
          auth: {
            email: 'nerd@nerd.nerd',
            password: 'nerdpassword'
          }
        }
      );
      //   alert('Your update has been made!');
      //   window.location.reload;
      console.log(res);
      //   this.$router.push(`/resources/${res.data.id}`);
    }
  }
};
</script>

<style scoped>
img {
  opacity: 900%;
  max-height: 200px;
  margin: 20px;
  justify-content: center;
  border-radius: 10px;
}
.showForm {
  visibility: visible;
  display: flex;
  align-items: start;
}
/* .container {
  display: grid;
  grid-template-columns: 1;
  align-items: center;
  margin: 20px;
  color: white;
} */

.submitBtn,
.updateBtn {
  width: 80px;
  height: 45px;
  margin: 10px;
  font-size: 15px;
  background-color: #122b3b;
  font-weight: bolder;
  cursor: pointer;
  border-radius: 10px;
  border: 4px solid;
  color: white;
}
.submitBtn:hover,
.updateBtn:hover {
  background-color: #e0b12f;
  color: white;
  cursor: pointer;
}
.deleteBtn {
  width: 50px;
  height: 45px;
  margin: 10px;
  font-size: 15px;
  background-color: #8d0000;
  font-weight: bolder;
  cursor: pointer;
  border-radius: 10px;
  border: 4px solid;
  color: rgba(255, 255, 255, 0.945);
}
a {
  color: rgb(255, 255, 255);
  padding: 10px;
}

.source {
  background-color: rgba(230, 218, 218, 0.425);
  padding: 10px;
  color: white;
  border-radius: 12px;
  max-height: 75px;
  max-width: 700px;
  white-space: pre-line;
}
.deleteBtn:hover {
  background-color: gray;
  color: white;
  cursor: pointer;
}
</style>
