<template lang="html">
  <form class="login form">
    <div class="field">
      <label for="id_username">Username</label>
      <input
        v-model="username"
        type="text"
        placeholder="Username"
        autofocus="autofocus"
        maxlength="150"
        id="id_username"
      />
    </div>
    <div class="field">
      <label for="id_password">Password</label>
      <input
        v-model="password"
        type="password"
        placeholder="Password"
        id="id_password"
      />
    </div>
    <button @click.prevent="authenticate" class="button primary" type="submit">
      Log In
    </button>
  </form>
</template>

<script>
// import axios from 'axios';

export default {
  name: 'Login',
  data() {
    return {
      username: '',
      password: ''
    };
  },
  methods: {
    authenticate() {
      //   const payload = {
      //     username: this.username,
      //     password: this.password
      //   };
    }
  }
};
</script>

<style>
input {
  width: 500px;
  height: 60px;
  margin: 10px;
}
</style>
