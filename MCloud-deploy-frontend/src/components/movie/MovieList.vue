<template>
  <div>
    <movie-filter></movie-filter>
    <div class="container">
      <movie-list-item
        v-for="(movie,idx) in pageMovies"
        :key="idx"
        :movie="movie"
      ></movie-list-item>
    </div>
    <movie-list-pagination 
      @page-data="getPageData"
      :max-page="getMaxPage"
    >
    </movie-list-pagination>
  </div>
</template>

<script>
import MovieFilter from '@/components/movie/MovieFilter'
import MovieListItem from '@/components/movie/MovieListItem'
import MovieListPagination from '@/components/movie/MovieListPagination'
import { mapState, mapGetters } from 'vuex'

export default {
  name: 'MovieList',
  components: {
    MovieListItem,
    MovieFilter,
    MovieListPagination,
  },
  data: function () {
    return {
      pageCnt: 1,
    }
  },
  computed: {
    ...mapState([
      'movies'
    ]),
    ...mapGetters([
      'filterMovies',
    ]),
    pageMovies: function () {
      let pageMovieList = []
      let start = (this.pageCnt - 1) * 16
      let end = start + 16
      pageMovieList = this.filterMovies.filter((movie,index) => {
        return (index >= start && index < end)
      })
      return pageMovieList
    },
    getMaxPage: function () {
      return parseInt(this.filterMovies.length / 16) + 1
    }
  },
  methods: {
    getPageData: function (page) {
      this.pageCnt = page
    }
  }
}
</script>

<style>
  .container {
    display: flex;
    flex-wrap: wrap;
  }
</style>