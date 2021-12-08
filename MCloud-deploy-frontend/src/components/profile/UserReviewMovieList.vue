<template>
  <div>
    <h2 class="my-profile-title">{{ $route.params.username }}'s watched Movie List</h2>
    <div class="container">
      <carousel
        class="my-carousel"
      >
        <slide
          v-for="movie in userReviewMovieList"
          :key="movie.id"
          class="my-slide"
        >
          <user-review-movie-list-item
            :movie="movie"
          >
          </user-review-movie-list-item>
        </slide>
      </carousel>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import UserReviewMovieListItem from '@/components/profile/UserReviewMovieListItem'

import { Carousel, Slide } from 'vue-carousel';





export default {
  name: 'UserReviewMovieList',
  components: { 
    UserReviewMovieListItem,
    Carousel,
    Slide,
  },
  computed: {
    ...mapState([
      'userReviewMovieList',
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