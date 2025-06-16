import { createRouter, createWebHistory } from 'vue-router'
import FilmList from '@/views/FilmList.vue'
import FilmDetail from '@/views/FilmDetail.vue'

const routes = [
  { path: '/', name: 'home', component: FilmList },
  { path: '/films', name: 'films', component: FilmList },
  { path: '/films/:id', name: 'film-detail', component: FilmDetail, props: true },
]

export default createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
})
