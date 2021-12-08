<template>
  <div class="search-list-box" @click="getMovieId" >
    {{ searchMovie.title }}
  </div>
</template>

<script>

export default {
  name: 'ReviewCreateSearch',
  props: {
    searchMovie: Object
  },
  methods: {
    getMovieId: function () {
      this.$emit('getMovieId', this.searchMovie)
    }
  }
}
</script>

<style>
  .search-list-box {
    text-align: left;
    padding: 1rem;
    width: 28rem;
    margin: 0 auto;
    cursor: pointer;
  }
</style>