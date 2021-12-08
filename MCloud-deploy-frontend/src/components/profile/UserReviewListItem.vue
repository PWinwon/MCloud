<template>
  <div>
    <hr style="margin: 0;">
    <div class="container" style="height: 50px; align-items: center;">
      <div class="son-id" @click="goUserProfile">{{review.user_id.username}}</div>
      <div class="son-movie-title" @click="goMovieDetail">
          {{ review.movie_id.title }}
      </div>
      <div class="son-title" @click="goReviewDetail">
        {{ review.title }}
      </div>
      <div class="son-rank" >
        <star-rating 
          v-if="review"
          :increment="0.5" 
          :inline="true" :star-size="20" 
          :read-only="true" :show-rating="false" 
          :rating="review.rank / 2"
          :inactive-color="'#ffffff'"
        ></star-rating> 
      </div>
      <div class="son-recommend"><i class="far fa-thumbs-up" style="color: white;">  {{ review.like_users.length }}</i></div>
      <div class="son-date">
        {{ review.created_at.substring(0,10)}}
      </div>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import StarRating from 'vue-star-rating'

export default {
  name: 'ReviewListItem',
  components: {
    StarRating
  },
  props: {
    review: Object
  },
  methods: {
    goReviewDetail: function () {
      this.$router.push({ name: 'ReviewDetail', params: { review_pk: this.review.id }})
    },
    goMovieDetail: function () {
      this.$router.push({ name: 'MovieDetail', params: {movie_pk: this.review.movie_id.id}})
    },
    goUserProfile: function () {
      this.$router.push({ name: 'Profile', params: {username: this.review.user_id.username}})
    }
  },
  // 날짜 자르기
  filters: {
    filterDate: function (data) {
      return data.substring(0, 10)
    }
  },
  // movie 받아오기 추가
  computed: {
    ...mapState([
      'movies'
    ])
  },
}
</script>

<style scoped>
  div div {
    font-family: 'Pretendard-Regular';
  }
  .son-id {
    flex: 1.25;
    font-weight: bold;
    cursor: pointer;
  }
  .son-movie-title {
    flex: 1.5;
    text-align: left;
    text-decoration: underline;
    cursor: pointer;
  }
  .son-title {
    flex: 2.5;
    text-align: left;
    text-decoration: underline;
    cursor: pointer;
  }
  .son-rank {
    flex: 1.25;
    text-align: center;
  }
  .son-recommend{
    flex: 1.25;
  }
  .son-date {
    flex:1.5;
  } 
  /* .review-box-title {
    text-align: left; 
    padding: 0.3rem;
    vertical-align: middle;
  } */
    .test {
      color: rgb(219, 219, 12);
    }
</style>