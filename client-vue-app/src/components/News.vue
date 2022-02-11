<template>
  <div>
    <h1>LATEST NEWS</h1>
    <!-- <div id="news" class="container">
      <div class="news-card">
        <h1>{{ news[0].title }}</h1>
        <h5>Author: {{ news[0].author }}</h5>

        <img :src="news[0].urlToImage" />
        <h5>{{ news[0].description }}</h5>
        <h5>source: {{ news[0].url }}</h5>
      </div>
      <div class="news-card">
        <h1>{{ news[1].title }}</h1>
        <h5>Author: {{ news[1].author }}</h5>

        <img :src="news[1].urlToImage" />
        <h5>{{ news[1].description }}</h5>
        <h5>source: {{ news[1].url }}</h5>
      </div>
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
h1 {
  color: #80cbc4;
}
.news-card {
  max-width: 300px;
  padding: 20px;
  display: flex;
  flex-direction: column;
  justify-content: center;
}
.container {
  text-transform: initial;
  display: flex;
  flex-wrap: wrap;
}
img {
  max-height: 200px;
  border-radius: 7px 7px 0 0;
}
</style>
