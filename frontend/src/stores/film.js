import { defineStore } from 'pinia'

export const useFilmStore = defineStore('film', {
  state: () => ({
    films: [],
  }),
  actions: {
    async fetchFilms() {
      const res = await fetch(import.meta.env.VITE_API_URL + '/films/')
      this.films = await res.json()
    },
  },
})
