import VueRouter from 'vue-router';
import Home from './pages/Home';
import Login from './components/Login';
import Post from './components/Post';
import News from './components/News';

const routes = [
  { path: '/', component: Home, name: 'Home' },
  { path: '/login', component: Login, name: 'Login' },
  { path: '/createpost', component: Post, name: 'Post' },
  { path: '/news', component: News, name: 'News' }
];

export default new VueRouter({ routes, mode: 'history' });
