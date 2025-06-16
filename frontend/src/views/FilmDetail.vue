<template>
  <v-container class="py-4" v-if="film">
    <!-- Bouton Retour -->
    <v-btn icon @click="goBack">
      <v-icon>mdi-arrow-left</v-icon>
    </v-btn>

    <!-- Titre du film -->
    <h1 class="text-h3 mb-2">{{ film.title }}</h1>

    <!-- Description editable -->
    <v-card class="mb-4 pa-4">
      <h2 class="text-h5 mb-2">Description</h2>
      <v-textarea
        v-model="editedDescription"
        auto-grow
        rows="3"
      />
      <v-btn class="mt-2" color="primary" @click="submitEdit">
        Enregistrer la description
      </v-btn>
    </v-card>

    <!-- Acteurs -->
    <v-card class="mb-4 pa-4">
      <h2 class="text-h5 mb-2">Acteurs</h2>
      <v-list dense>
        <v-list-item v-for="actor in film.actors" :key="actor.id">
          {{ actor.first_name }} {{ actor.last_name }}
        </v-list-item>
      </v-list>
    </v-card>

    <!-- Note moyenne -->
    <v-card class="mb-4 pa-4">
      <h2 class="text-h5 mb-2">
        Note moyenne : 
        <v-chip color="amber" text-color="black">
          ⭐ {{ film.average_rating.toFixed(1) }}
        </v-chip>
      </h2>
    </v-card>

    <!-- Liste des avis -->
    <v-card class="mb-4 pa-4">
      <h2 class="text-h5 mb-2">Avis</h2>
      <v-list two-line>
        <v-list-item v-for="rev in film.reviews" :key="rev.id">
          <v-list-item-content>
            <v-list-item-title>⭐ {{ rev.rating }}</v-list-item-title>
            <v-list-item-subtitle>{{ rev.description }}</v-list-item-subtitle>
            <v-list-item-subtitle class="text-caption grey--text">
              {{ new Date(rev.created_at).toLocaleString() }}
            </v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-card>

    <!-- Formulaire d’ajout d’avis -->
    <v-card class="pa-4">
      <h2 class="text-h5 mb-2">Ajouter un avis</h2>
      <v-form @submit.prevent="submitReview">
        <v-row>
          <v-col cols="12" md="3">
            <v-select
              v-model="newRating"
              :items="[1,2,3,4,5]"
              label="Note"
              required
            />
          </v-col>
          <v-col cols="12" md="9">
            <v-textarea
              v-model="newComment"
              label="Commentaire"
              auto-grow
              rows="2"
            />
          </v-col>
        </v-row>
        <v-btn color="success" type="submit">Envoyer</v-btn>
      </v-form>
    </v-card>
  </v-container>

  <!-- Loading or not found -->
  <v-container v-else class="py-4">
    <v-progress-circular indeterminate />
  </v-container>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { storeToRefs } from 'pinia'
import { useFilmStore } from '@/stores/film'


const route = useRoute()
const router = useRouter()
const filmId = route.params.id


const store = useFilmStore()
const { currentFilm: film } = storeToRefs(store)


const editedDescription = ref('')
const newRating = ref(5)
const newComment = ref('')


onMounted(async () => {
  await store.fetchFilm(filmId)
  if (store.currentFilm) {
    editedDescription.value = store.currentFilm.description
  }
})


watch(() => store.currentFilm, (f) => {
  if (f) editedDescription.value = f.description
})


function goBack() {
  router.back()
}


async function submitEdit() {
  await store.updateMovie(filmId, { description: editedDescription.value })
}


async function submitReview() {
  if (!newRating.value) return
  await store.addReview(filmId, newRating.value, newComment.value)
  // Réinitialiser le formulaire
  newRating.value = 5
  newComment.value = ''
}
</script>

<style scoped>
.v-card {
  border-radius: 8px;
}
</style>
