<template>
  <div id="news">
    <!-- <div>
      <h5>{{ news[0].title }}</h5>
      <h5>Author: {{ news[0].author }}</h5>

      <img :src="news[0].urlToImage" />
      <h5>{{ news[0].description }}</h5>
      <h5>source: {{ news[0].url }}</h5>
    </div> -->
  </div>
</template>

<script>
// import axios from 'axios';
// const API_KEY = process.env.VUE_APP_API_KEY;
export default {
  name: 'News',
  data: () => ({
    news: Object
  }),
  mounted() {
    // this.getNews();
  },
  methods: {
    // async getNews() {
    //   const res = await axios.get(
    //     `https://newsapi.org/v2/everything?q=neuroscience&apiKey=9b14a33f320e44b8a1906e3619bb679f`
    //   );
    //   this.news = res.data.articles;
    //   console.log(this.news);
    // }
  }
};
</script>

<style scoped>
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

img {
  max-height: 200px;
  border-radius: 7px 7px 0 0;
}
</style>
