<template>
  <div>
    <h2 class="my-profile-title">{{ $route.params.username }}'s Like Movie List</h2>
    <div class="container">
      <carousel
        class="my-carousel"
      >
        <slide
          v-for="movie in userLikeMovieList"
          :key="movie.id"
          class="my-slide"
        >
          <user-like-movie-list-item
            :movie="movie"
          >
          </user-like-movie-list-item>
        </slide>
      </carousel>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import UserLikeMovieListItem from '@/components/profile/UserLikeMovieListItem'

import { Carousel, Slide } from 'vue-carousel';

export default {
  name: 'UserLikeMovieList',
  components: {
    UserLikeMovieListItem,
    Carousel,
    Slide,
  },
  computed: {
    ...mapState([
      'userLikeMovieList',
    ])
  }

}
</script>

<style scoped>

.my-carousel {
  width: 40%;
}

.my-slide {
  align-items: center;
  display: flex;
  font-size: 1.5rem;
  justify-content: center;
  min-height: 10rem;
}

.my-profile-title {
  color: lightgray;
}

</style>