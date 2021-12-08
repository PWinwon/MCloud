<template>
  <div v-if="movie" class="grand-parent-box">
    <div class="parent-box">
      <div class="container">
        <div style="flex: 1;">
          <img :src="moviePosterPath" alt="poster" class="img-size">
        </div>
        <div style="flex: 1;">
          <h1 style="text-align: left;">{{ movie.title }} ({{ movie.release_date.substring(0,4)}})</h1>
          <movie-detail-cloud
            class="cloud-box"
            :keywords="movie.movie_keywords"
          ></movie-detail-cloud>
        </div>
      </div>
      <section class="detail-box">
        <div class="additional-box" style="margin-bottom: 1em;">
          <div class="additional-info">
            장르:
            <span
              v-for="(genres,idx) in movie.genres"
              :key="idx"
            >
            {{ genres.name }} |
            </span> 
          </div>
          <div class="additional-info">개봉일자: {{ movie.release_date.substring(0,10)}}</div>
        </div>
        <div>
          <hr>
        </div>
        <p style="font-size: 1.5rem;">줄거리</p>
        <p>{{ movie.overview }}</p>
        <div class="rank-box additional-info">
          <p>평점: {{ movie.vote_average }}</p>
          <p>투표: {{movie.vote_count}}명</p>
        </div>
      </section>
      <h3 class="left container" style="justify-content: space-between; font-size: 1.5rem; margin-bottom: 0.5rem;">
        Review
        <button @click="setReview" class="vue-btn">리뷰 작성 <i class="fas fa-arrow-right"></i></button>
      </h3>
      <div>
        <hr>
      </div>
      <div v-if="movie.movie_to_review.length != 0">
        <movie-detail-review 
          v-for="review in slicedReview"
          :key="review.pk"
          :review="review"
        ></movie-detail-review>
      </div>
      <div v-else>
        <p style="height: 2rem; padding: auto 0; font-size: 1.25rem;">리뷰를 작성해주세요.</p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { mapState } from 'vuex'

import MovieDetailReview from '@/components/movie_detail/MovieDetailReview'
import MovieDetailCloud from '@/components/movie_detail/MovieDetailCloud'

export default {
  name: 'MovieDetail',
  components: {
    MovieDetailReview,
    MovieDetailCloud
  },
  data: function () {
    return {
      movie: null,
      movieReview: null,
      moviePosterPath: null
    }
  },
  methods: {
    setReview: function () {
      this.$store.dispatch('getMovieForReviewCreate', this.movie)
      this.$router.push({ name: 'ReviewCreate'})
    }
  },
  created: function () {
    axios ({
      method: 'get',
      url: `${this.tmpUrl}/movies/movie/${this.$route.params.movie_pk}`,
    })
    .then(res => {
      this.movie = res.data
      this.movieReview = res.data.movie_to_review.reverse()
      this.moviePosterPath = `https://image.tmdb.org/t/p/w500/${this.movie.poster_path}`
    })
    .catch(err => {
      console.log(err)
    })
  },
  computed: {
    ...mapState([
      'tmpUrl'
    ]),
    slicedReview: function () {
      if (this.movieReview) {
        const newReview = this.movieReview.filter((review, idx) => {
          return idx < 5
        }) 
        return newReview
      } else {
        return []
      }
    }
  }
}
</script>

<style scoped>
  p {
    margin: 0.25em 0.5em;
  }
  .grand-parent-box {
    display: flex;
    justify-content: center;
    padding: 3rem;
    border-radius: 1%;
    width: 70rem;
    margin: 0 auto;
    background-color: #bed8f548;;
  }
  .parent-box {
    width: 60rem;
    display: flex;
    flex-direction: column;
  }
  .container {
    display: flex;
  }
  .img-size {
    width: 20em;
    height: auto;
    border-radius: 10px;
  }

  .vue-btn {
    background-color: rgb(168, 210, 238);
    color: rgb(38, 0, 255);
    border: none;
    border-radius: 0.5rem;
    width: 6rem;
    height: 2.5rem;
    font-size: 1rem;
    font-weight: bold;
    font-family: 'Pretendard-Regular';
  }

  .detail-box {
    text-align: left;
    padding: 1rem 0;
    margin: 1em 0;
    display: flex;
    flex-direction: column;
    border: 2px solid white;
    border-radius: 1.5em;
  }
  .font-face {
    font-family: 'OTWelcomeBA';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2110@1.0/OTWelcomeBA.woff2') format('woff2');
    font-weight: normal;
    font-style: normal;
  }
  div div {
    color: white;
    font-family: 'Pretendard-Regular';
  }
  .cloud-box {
    border: 1px solid white;
    border-radius: 2rem;
    width: 20rem;
    height: 20rem;
    padding: 2rem;
    display: flex;
    flex-direction: column;
    justify-content: center;
  }
  .rank-box {
    text-align: right;
    text-decoration: underline;
    margin-right: 1rem;
    display: flex;
    flex-direction: column;
  }
  .additional-box {
    display: flex;
  }
  .additional-info {
    font-size: 1.1em;
    margin: 0 0.5em;
  }
</style>