<template>
  <div>
    <user-like-movie-list></user-like-movie-list>
    <user-review-movie-list></user-review-movie-list>
    <div class="review-box">
      <user-review-list></user-review-list>
    </div>
  </div>
</template>

<script>
import UserLikeMovieList from '@/components/profile/UserLikeMovieList'
import UserReviewList from '@/components/profile/UserReviewList'
import UserReviewMovieList from '@/components/profile/UserReviewMovieList'



export default {
  name: 'Profile',
  components: {
    UserLikeMovieList,
    UserReviewList,
    UserReviewMovieList,
  },
  created: function () {
    this.$store.dispatch('getUserLikeMovieList', this.$route.params.username)
  }
}
</script>

<style scoped>
  .review-box {
    border: 2px solid white;
    border-radius: 10px;
    width: 72rem;
    height: auto;
    margin: 10vh auto 10vh;
    color: rgb(240, 240, 240);
    background: #bed8f548;
  }

</style>