<template>
  <div>
    <!-- <vs-card type="2" @click="goMovieDetail" style="padding: 10px;"> -->
    <vs-card type="2" style="padding: 10px;">
      <template #title>
        <h3 @click="goMovieDetail">{{ movie.title }}</h3>
      </template>
      <template #img>
        <img :src="getPoster()" alt="poster" @click="goMovieDetail">
      </template>
      <template #text>
        <p @click="goMovieDetail">
          {{ movie.overview | setOverview }}
        </p>
      </template>
      <template #interactions>
        <vs-button v-if="likeStatus" icon style="background-color: white;">
          <i class="fas fa-heart" style="color: red;"></i>
        </vs-button>        
        <vs-button v-else icon style="background-color: white;">
          <i class="far fa-heart" style="color: red;"></i>
        </vs-button>
        <vs-button class="btn-chat" shadow primary>
          <i class='bx bx-chat' ></i>
          <span class="span">
            {{ movie.like_count }}
          </span>
        </vs-button>
      </template>
    </vs-card>
  </div>
</template>

<script>
import Vue from 'vue'
import Vuesax from 'vuesax'
import 'vuesax/dist/vuesax.css'
import { mapState } from 'vuex'

Vue.use(Vuesax, {

})

export default {
  name: 'UserReviewMovieListItem',
  props: {
    movie: Object
  },
  methods: {
    getPoster: function () {
      return `https://image.tmdb.org/t/p/w185/${this.movie.poster_path}`
    },
    goMovieDetail: function () {
      this.$router.push({ name: 'MovieDetail', params: {movie_pk: this.movie.id}})
    },
  },
  filters: {
    setOverview: function (data) {
      return data.substring(0, 30) + '...'
    }
  },
  computed: {
    ...mapState([
      'loginUser',
    ]),
    likeStatus: function () {
      for (const user of this.movie.movie_like_users) {
        if (user.username === this.loginUser) {
          return true
        }
      }
      return false
    },
  }
}
</script>

<style>

</style>