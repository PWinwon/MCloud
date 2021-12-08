<template>
  <div style="margin: 4em 40px;">
    <movie-search></movie-search>
    <br>
    <movie-list></movie-list>

  </div>
</template>

<script>
import MovieList from '@/components/movie/MovieList'
import MovieSearch from '@/components/movie/MovieSearch'

export default {
  name: 'Movie',
  components: {
    MovieList,
    MovieSearch
  },
  created: function () {
    this.$store.dispatch('getMovies')
  }
}
</script>

<style>

</style>