<template>
  <div class="resource-container">
    <div class="container">
      <img
        :src="resource_card.image"
        alt="picture"
        :class="picclass"
        @mouseover="mouseon"
        @mouseleave="mouseoff"
      />
      <div v-if="showName" class="center">
        {{ resource_card.topic }} {{ resource_card.content }}
        {{ resource_card.link }}
      </div>
    </div>
    <div @click="deleteImage" class="deleteBtn">x</div>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'ResourceCard',
  data: () => ({
    showName: false,
    picclass: 'normal'
  }),
  props: {
    resource_card: Object
  },
  methods: {
    async deleteImage() {
      await axios.delete(
        `http://localhost:8000/resources/${this.resource_card.id}`,
        {
          auth: {
            username: 'nerduser',
            password: 'nerdpassword'
          }
        }
      );
      this.$emit('handleDelete', this.resource_card.id);
    },
    mouseon() {
      this.showName = true;
      this.picclass = 'blur';
    },
    mouseoff() {
      this.showName = false;
      this.picclass = 'normal';
    }
  }
};
</script>

<style scoped>
img {
  max-height: 200px;
  border-radius: 7px 7px 0 0;
}

.container {
  position: relative;
  display: flex;
  justify-content: center;
}

.center {
  position: absolute;
  top: 50%;
  text-align: center;
  font-size: 22px;
  color: black;
}

img {
  width: 100%;
  height: auto;
}

.blur {
  opacity: 0.6;
}

.resource-container {
  width: 300px;
  margin-bottom: 10px;
}

.deleteBtn {
  width: 100%;
  background-color: #80cbc4;
  font-size: 20px;
  font-weight: 700;
  cursor: pointer;
  border-radius: 0 0 7px 7px;
}

.deleteBtn:hover {
  background-color: #682424;
  color: white;
}
</style>
