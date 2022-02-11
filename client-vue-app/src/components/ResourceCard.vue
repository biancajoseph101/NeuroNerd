<template>
  <div class="resource-container">
    <div class="container">
      <img :src="resource_card.image" alt="picture" />
      <h5 class="source">
        SOURCE: <a href="#">{{ resource_card.link }} </a>
      </h5>
      <div>
        <h2>
          {{ resource_card.topic }}
        </h2>
      </div>

      <br />
      <div>{{ resource_card.content }}</div>
      <div class="showForm">
        <button @click="showForm = !showForm" class="updateBtn">edit</button>
        <div v-if="showForm" class="form-container">
          <form>
            <input
              placeholder="new topic name"
              :value="newTopic"
              name="newTopic"
              type="text"
              v-on:input="handleFormChange"
            /><br />
            <button @click="updateResource" class="submitBtn">submit</button>
          </form>
          <button @click="deleteResource" class="deleteBtn">x</button>
        </div>
        <div v-else></div>
      </div>
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
.form-container {
  visibility: colllapse;
}
.container {
  display: flex;
  justify-content: center;
  align-items: center;
}
img {
  opacity: 900%;
  max-height: 200px;
  margin: 20px;
  justify-content: center;
}
.showForm {
  visibility: visible;
}
.container {
  display: grid;
  grid-template-columns: 1;
  align-items: center;
  margin: 20px;
}
.updateBtn {
  width: 100px;
  height: 30px;
  background-color: #6ab3e4;
  font-size: 20px;
  font-weight: 700;
  cursor: pointer;
  border-radius: 4px;
}
.updateBtn:hover {
  background-color: #20af2c;
  color: white;
}
.submitBtn {
  width: 100px;
  height: 30px;
  background-color: #6ab3e4;
  font-size: 20px;
  font-weight: 700;
  cursor: pointer;
  border-radius: 4px;
}
.submitBtn:hover {
  background-color: #20af2c;
  color: white;
}
.deleteBtn {
  width: 50px;
  height: 30px;
  background-color: #991111;
  font-size: 20px;
  font-weight: 700;
  cursor: pointer;
  border-radius: 4px;
}
a {
  color: rgb(16, 7, 100);
}
.deleteBtn:hover {
  background-color: #ff0000;
  color: white;
}
</style>
