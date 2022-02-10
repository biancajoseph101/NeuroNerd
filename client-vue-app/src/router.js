import VueRouter from 'vue-router';
import Home from './pages/Home';
import Login from './components/Login';
import Post from './components/Post';
import News from './components/News';
import ResourceType from './pages/ResourceType';
import ResourceForm from './pages/ResourceForm';
import ResourceDrop from './components/ResourceDrop';
import Article from './pages/Article';

const routes = [
  { path: '/', component: Home, name: 'Home' },
  { path: '/login', component: Login, name: 'Login' },
  { path: '/createpost', component: Post, name: 'Post' },
  { path: '/createresource', component: ResourceForm, name: 'ResourceForm' },
  { path: '/news', component: News, name: 'News' },
  { path: '/articles', component: Article, name: 'Article' },
  { path: '/resourcedrop', component: ResourceDrop, name: 'ResourceDrop' },
  {
    path: '/resources/:resource_id',
    component: ResourceType,
    name: 'ResourceType'
  }
];

export default new VueRouter({ routes, mode: 'history' });
