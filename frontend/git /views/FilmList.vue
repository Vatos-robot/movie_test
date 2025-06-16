<template>
  <v-container class="py-4">
    <h1 class="text-h4 mb-4">Films</h1>

    <v-list two-line>
      <v-list-item
        v-for="film in films"
        :key="film.id"
        :to="{ name: 'film-detail', params: { id: film.id } }"
        link
      >
        <v-list-item-content>
          <v-list-item-title>{{ film.title }}</v-list-item-title>
          <v-list-item-subtitle>
            ⭐ {{ film.average_rating.toFixed(1) }}
          </v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>
    </v-list>

    <div class="d-flex justify-space-between mt-4">
      <v-btn @click="navigate(prev)" :disabled="!prev">Précédent</v-btn>
      <v-btn @click="navigate(next)" :disabled="!next">Suivant</v-btn>
    </div>
  </v-container>
</template>

<script setup>
import { onMounted } from 'vue'
import { storeToRefs } from 'pinia'
import { useFilmStore } from '@/stores/film'

const store = useFilmStore()
const { films, next, prev } = storeToRefs(store)

// Charge la première page au montage
onMounted(() => {
  store.fetchFilms()
})

function navigate(url) {
  if (!url) return
  // On veut juste le chemin et les query params
  const u = new URL(url)
  const pathAndQuery = u.pathname + u.search
  store.fetchFilms(pathAndQuery)
}
</script>

<style scoped>

</style>
