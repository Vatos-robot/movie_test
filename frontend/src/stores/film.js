import { defineStore } from 'pinia'
import axios from 'axios'

const API = axios.create({
  baseURL: import.meta.env.VITE_API_URL || 'http://localhost:8000/api'
})

export const useFilmStore = defineStore('film', {
  state: () => ({
    films: [],
    next: null,
    prev: null,
    currentFilm: null,
  }),
  actions: {
    async fetchFilms(pathOrUrl = '/movies/') {
      let res
      if (pathOrUrl.startsWith('http')) {
        res = await axios.get(pathOrUrl)
      } else {
        res = await API.get(pathOrUrl)
      }
      this.films = res.data.results
      this.next  = res.data.next
      this.prev  = res.data.previous
    },

    async fetchFilm(id) {
      const res = await API.get(`/movies/${id}/`)
      this.currentFilm = res.data
    },

    async addReview(movieId, rating, description) {
      await API.post('/reviews/', { movie: movieId, rating, description })
      await this.fetchFilm(movieId)
    },


    async updateMovie(id, data) {
      await API.patch(`/movies/${id}/`, data)
      await this.fetchFilm(id)
    },
  },
})
