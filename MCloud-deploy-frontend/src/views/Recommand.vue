<template>
  <div class="my-recommand">
    <br>
    <recommand-movie-list-first></recommand-movie-list-first>
  </div>
</template>

<script>
import RecommandMovieListFirst from '@/components/recommand/RecommandMovieListFirst'


export default {
  name: 'Recommand',
  components: {
    RecommandMovieListFirst,
  },
  created: function () {
    this.$store.dispatch('getRecommandMoviesByLikeGenre')
  }
}
</script>

<style scoped>

.my-recommand {
  margin-top: 13vh;
}


</style>