<template>
  <div class="parents-box">
    <div class="top-box">
      <div style="text-align: left;">
        <textarea name="searchKeyword" cols="50" rows="2" placeholder="🔍︎영화 검색" class="title" v-model="searchKeyword" @click="searchIn" v-click-outside="searchOut"></textarea>
        <div v-if="searchKeyword && isSearching" class="search-movie-box">
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
      <div v-if="isMovieEmpty" class="submit-err" style="top: 4rem; left:1rem;">
        올바른 영화를 선택해주세요.
      </div>
      <div class="rank-box">
        평점: {{review_input.rank * 2}}
        <star-rating 
          :border-width="4"
          :increment="0.5"
          :star-size="20"
          border-color="#d8d8d8" 
          :rounded-corners="true" 
          :show-rating="false"
          :star-points="[23,2, 14,17, 0,19, 10,34, 7,50, 23,43, 38,50, 36,34, 46,19, 31,17]"
          class="star-section"
          v-model="review_input.rank"
        ></star-rating>
      </div>
    </div>
    <div style="margin: 0 0.8em;">
      <textarea name="title" cols="80" rows="2" placeholder="제목" class="title" v-model.trim="review_input.title"></textarea>
    </div>
    <div v-if="isTitleEmpty" class="submit-err" style="top: 14rem; right:4.5rem;">
      제목을 입력해주세요.
    </div>
    <div style="margin: 0 0.8em;">
      <textarea name="content" cols="80" rows="20" placeholder="내용" class="content" v-model.trim="review_input.content"></textarea>
    </div>
    <div v-if="isContentEmpty" class="submit-err" style="top: 43rem; right:4.5rem;">
      내용을 입력해주세요.
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
  name: 'ReviewCreate',
  directives: {
    clickOutside: vClickOutside.directive
  },
  components: {
    StarRating,
    ReviewCreateSearch,
  },
  data: function () {
    return {
      review_input: {
        title: '',
        content: '',
        rank: 0,
      },
      searchKeyword: null,
      isSearching: false,
      movie: null,
      movieId: null,
      isMovieEmpty: false,
      isTitleEmpty: false,
      isContentEmpty: false,
    }
  },
  methods: {
    setReview: function () {
      this.isMovieEmpty = false
      this.isTitleEmpty = false
      this.isContentEmpty = false
      axios({
        method: 'post',
        url: `${this.tmpUrl}/community/movie/${this.movieId}/review/`,
        data: {
          ...this.review_input,
          rank: this.review_input.rank * 2
        },
        headers: this.header
      })
      .then((res) => {
        this.$router.push({ name: 'ReviewDetail', params:{review_pk: res.data.id}})
      })
      .catch(err => {
        if (this.review_input.title != '' && this.review_input.content != '') {
          this.isMovieEmpty = true
        } else {
           if (this.review_input.title === '') {
            this.isTitleEmpty = true
          } if (this.review_input.content === '') {
              this.isContentEmpty = true
          }
        }
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
      this.isMovieEmpty = false,
      this.searchKeyword = searchMovie.title
      this.movieId = searchMovie.id
    }
  },
  created: function () {
    if (this.movieForReviewCreate) {
      this.movie = this.movieForReviewCreate
      this.searchKeyword = this.movie.title
      this.movieId = this.movie.id
    }
  },
  computed: {
    ...mapState([
      'tmpUrl',
      'header',
      'movies',
      'movieForReviewCreate'
    ]),
    searchMovies: function () {
      if (this.searchKeyword) {
        const relatedMovie = this.movies.filter(movie => {
          return (movie.title.includes(this.searchKeyword))
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
    position: relative;
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
    margin: 0 0.8em;
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
  .submit-position {
    position: relative;
  }
  .submit-err {
    color: red;
    position: absolute;
  }
</style>