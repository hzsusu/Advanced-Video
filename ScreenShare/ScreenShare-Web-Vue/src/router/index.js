import Vue from 'vue'
import VueRouter from 'vue-router'
import routes from './routes'

Vue.use(VueRouter)

const router = new VueRouter({
    mode: 'hash',
    base: process.env.BASE_URL,
    routes: [{
      path: '/',
      name: 'join',
      component: () => import( /* webpackChunkName: "join" */ '../views/join/index.vue')
    }].concat(routes)
})

router.onError((error) => {
  const pattern = /Loading chunk (\w)+ failed/g;
  const isChunkLoadFailed = error.message.match(pattern);
  const targetPath = router.history.pending.fullPath;
  if (isChunkLoadFailed) {
     router.replace(targetPath);
  }
})

export default router
