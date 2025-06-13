// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import FilmList from '@/views/FilmList.vue'
import FilmDetail from '@/views/FilmDetail.vue'

const routes = [
  { path: '/', name: 'home', component: HomeView },
  { path: '/films', name: 'films', component: FilmList },
  { path: '/films/:id', name: 'film-detail', component: FilmDetail, props: true },
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
})

export default router
