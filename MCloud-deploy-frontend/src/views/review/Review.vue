<template>
  <div>
    <div class="container" style="justify-content: space-between; align-items: center; width: 72rem; margin: 2em auto;">
      <review-search></review-search>
      <button @click="goReviewCreate" class="submit-btn">리뷰 작성</button>
    </div>
    <div class="review-box">
      <review-list></review-list>
    </div>
  </div>
</template>

<script>
import ReviewList from '@/components/review/ReviewList'
import ReviewSearch from '@/components/review/ReviewSearch'

export default {
  name: 'Review',
  components: {
    ReviewList,
    ReviewSearch
  },
  methods: {
    goReviewCreate: function () {
      this.$store.dispatch('removeMovieForReviewCreate')
      this.$router.push({ name: 'ReviewCreate' })
    }
  },
  created: function () {
    this.$store.dispatch('getReviews')
  },
}
</script>

<style scoped>
  .review-box {
    border: 2px solid white;
    border-radius: 10px;
    width: 72rem;
    height: auto;
    margin: 0 auto 10vh;
    color: rgb(240, 240, 240);
    background: #bed8f548;
  }
  .submit-btn {
    background-color: #edbf4293;
    color: rgb(214, 214, 214);
    font-weight: bold; 
    display: inline;
    width: 5.5em;
    height: 3em;
    border: none;
    border-radius: 1em;
    font-family: 'Pretendard-Regular';
  }
</style>