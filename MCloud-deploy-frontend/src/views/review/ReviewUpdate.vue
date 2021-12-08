<template>
  <div class="parents-box">
    <div class="top-box">
      <div style="text-align: left;">
        <textarea name="searchKeyword" cols="50" rows="2" placeholder="🔍︎영화 검색" class="title" v-model="reviewUpdateData.movieTitle" @click="searchIn" v-click-outside="searchOut"></textarea>
        <div v-if="reviewUpdateData.movieTitle && isSearching" class="search-movie-box">
          <div v-if="searchMovies.length">
            <review-create-search 
              v-for="searchMovie in searchMovies"
              :key="searchMovie.id"
              :searchMovie="searchMovie"
              @getMovieId="getMovieId"
            ></review-create-search>
          </div>
          <div v-else class="if-empty">
            해당 영화 없음
          </div>
        </div>
      </div>
      <div class="rank-box">
        평점: {{reviewUpdateData.rank * 2}}
        <star-rating 
          :border-width="4"
          :increment="0.5"
          :star-size="20"
          border-color="#d8d8d8" 
          :rounded-corners="true" 
          :show-rating="false"
          :star-points="[23,2, 14,17, 0,19, 10,34, 7,50, 23,43, 38,50, 36,34, 46,19, 31,17]"
          class="star-section"
          v-model="reviewUpdateData.rank"
        ></star-rating>
      </div>
    </div>
    <div>
      <textarea name="title" cols="80" rows="2" placeholder="제목" class="title" v-model="reviewUpdateData.title"></textarea>
    </div>
    <div>
      <textarea name="content" cols="80" rows="20" placeholder="내용" class="content" v-model="reviewUpdateData.content"></textarea>
    </div>
    <button @click="setReview" class="review-create-btn">작성</button>
  </div>
</template>

<script>
import axios from 'axios'
import { mapState } from 'vuex'

import vClickOutside from 'v-click-outside'

import StarRating from 'vue-star-rating'
import ReviewCreateSearch from '@/components/review_create/ReviewCreateSearch'

export default {
  name: 'ReviewUpdate',
  directives: {
    clickOutside: vClickOutside.directive
  },
  components: {
    StarRating,
    ReviewCreateSearch,
  },
  data: function () {
    return {
      searchKeyword: null,
      isSearching: false,
    }
  },
  methods: {
    setReview: function () {
      axios({
        method: 'put',
        url: `${this.tmpUrl}/community/movie/${this.reviewUpdateData.movieId}/review/${this.reviewUpdateData.review_pk}/`,
        data: {
          title: this.reviewUpdateData.title,
          content: this.reviewUpdateData.content,
          rank: this.reviewUpdateData.rank * 2,
        },
        headers: this.header
      })
      .then(() => {
        this.$router.push({ name: 'ReviewDetail', params:{review_pk: this.reviewUpdateData.review_pk}})
      })
      .catch(err => {
        console.log(err)
      })
    },
    searchIn: function () {
      this.isSearching = true
    },
    searchOut: function () {
      this.isSearching = false
    },
    getMovieId: function (searchMovie) {
      this.reviewUpdateData.movieTitle = searchMovie.title
      this.reviewUpdateData.movieId = searchMovie.id
    }
  },
  created: function () {
    if (this.$route.params.title) {
      this.$store.dispatch('reviewUpdateSave', {
        review_pk: this.$route.params.review_pk,
        title:  this.$route.params.title,
        content: this.$route.params.content,
        rank: this.$route.params.rank,
        movieTitle: this.$route.params.movieTitle,
        movieId: this.$route.params.movieId
      })
    }

  },
  computed: {
    ...mapState([
      'tmpUrl',
      'header',
      'movies',
      'reviewUpdateData'
    ]),
    searchMovies: function () {
      if (this.reviewUpdateData.movieTitle) {
        const relatedMovie = this.movies.filter(movie => {
          return (movie.title.includes(this.reviewUpdateData.movieTitle))
        })
        return relatedMovie
      } else {
        return []
      }
    }
  }
}
</script>

<style scoped>
  .parents-box {
    padding: 3rem;
    margin: 0 auto;
    width: 48.5rem;
    height: 55rem;
    border-radius: 2rem;
    padding-top: 3rem;
  }
  
  /* .review-create-grid {
    display: grid;
    grid-template-rows: 1fr 8fr 1fr 1fr 1fr;
  } */

  textarea {
    border: 1px solid lightgray;
    border-radius: 1rem;
    font-family: 'Pretendard-Regular';
    padding: 1rem;
    margin: 1rem 0;
  }

  .title {
    font-size: 17px;
  }

  .top-box {
    display: grid;
    grid-template-columns: 2fr 1fr;
    position: relative;
  }

  .rank-box {
    display: flex;
    justify-content: space-evenly;
    align-items: center;
    border: 1px solid lightgray;
    border-radius: 1rem;
    font-family: 'Pretendard-Regular';
    margin: 1rem 0 1rem 1rem;
    background-color: white;
  }

  .content {
    font-size: 17px;
  }

  .review-create-btn {
    font-family: 'Pretendard-Regular';
    color: white;
    font-size: 1rem;
    border: none;
    border-radius: 2rem;
    background-color: rgb(123, 201, 221);
    width: 8rem;
    height: 4rem;
    margin-top: 2rem;
  }
  
  .search-movie-box {
    position: absolute;
    top: 6rem;
    border: 1px solid lightgray;
    border-radius: 1rem;
    width: 31rem;
    background-color: white;
  }
  .if-empty {
    height: 3rem; 
    display: flex;
    flex-direction: column;
    font-family: 'Pretendard-Regular';
    justify-content: center;
  }
</style>