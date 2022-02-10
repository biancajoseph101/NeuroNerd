<template>
  <div class="resource-container">
    <div class="container">
      <img :src="resource_card.image" alt="picture" />
      <div>
        <h2>
          {{ resource_card.topic }}
        </h2>
      </div>
      <div>
        <h5 class="source">
          SOURCE: <a href="#">{{ resource_card.link }} </a>
        </h5>
      </div>
      <div>{{ resource_card.content }}</div>
      <div>
        <button @click="showForm" class="updateBtn">edit</button>
        <div class="form-container">
          <form>
            <input
              placeholder="new topic name"
              :value="newTopic"
              name="newTopic"
              type="topic"
              v-on:input="handleFormChange"
            />
            <button @click="updateResource" class="submitBtn">submit</button>
          </form>
          <button @click="deleteResource" class="deleteBtn">x</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'ResourceCard',
  data: () => ({
    showForm: true,
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
    },
    async updateResource(e) {
      e.preventDefault();
      const res = await axios.put(
        `http://localhost:8000/resources/${this.resource_card.id}`,
        {
          showForm: true,
          topic: this.newTopic
        },
        {
          auth: {
            email: 'nerd@nerd.nerd',
            password: 'nerdpassword'
          }
        }
      );
      this.$router.push(`/resources/${res.data.id}`);
      this.$emit('handleUpdate', this.resource_card.id);
    }
  }
};
</script>

<style scoped>
img {
  max-height: 200px;
  margin: 20px;
}

.container {
  display: flex;
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
