<template>
  <div style="text-align: center;">
    <div v-if="reviewDetail" class="review-box">
      <h1 style="padding: 1rem 0 0 2rem;">"{{ reviewDetail.movie_id.title}}"</h1>
      <div class="devine-box container" style="position: relative; justify-content: space-between; padding: 0 2rem;">
        <p style="margin: 0; align-self: center;">작성자: {{ reviewDetail.user_id.username }}</p>
        <div class="container" style="flex-direction: column;">
          <div class="review-date">작성: {{ reviewDetail.created_at | filterDate}} {{ reviewDetail.created_at | filterTime}}</div>
          <div class="review-date">수정: {{ reviewDetail.updated_at | filterDate}} {{ reviewDetail.updated_at | filterTime}}</div>
        </div>
      </div>
      <div style="padding-left: 2rem;">
        <div class="container" style="justify-content: space-between;">
          <p style="font-weight: bold;">{{ reviewDetail.title }}</p>
          <star-rating 
            v-if="reviewDetail"
            :increment="0.5" 
            :inline="true" :star-size="20" 
            :read-only="true" :show-rating="false" 
            :rating="reviewDetail.rank / 2"
            :inactive-color="'#ffffff'"
            style="padding-right: 2rem;"
          ></star-rating>          
        </div>
        <p class="review-content">{{ reviewDetail.content }}</p>
      </div>
      <div class="container" style="justify-content: space-between; padding: 1rem 0;">
        <div>
          <vs-button @click="reviewLike" :active="likeClickedOrNot" type="border" :class="{'is-liked': likeClickedOrNot, 'is-not-liked': !likeClickedOrNot}">
            <i class="far fa-thumbs-up fa-lg" :class="{'i-true': likeClickedOrNot, 'i-false': !likeClickedOrNot}"> {{ reviewDetail.like_count}}</i>
            </vs-button>
        </div>
        <!-- <div v-else>
          <vs-button @click="reviewLike" color="rgb(255, 255, 255)" type="border" style="margin-left: 2rem;"><i class="far fa-thumbs-up fa-lg" style="color: blue;"> {{ reviewDetail.like_count}}</i></vs-button>
        </div> -->
        <div v-if="reviewDetail.user_id.username === loginUser" style="margin-right: 2em;">
          <button class="rd-button" @click="updateReview">수정</button>
          <button class="rd-button" @click="deleteReview">삭제</button>
        </div>
      </div>
      <div class="devine-box container" style="justify-content: flex-start; align-items: center; padding: 0 2rem; margin-bottom: 0.5em">
        <p style="margin:0;">댓글</p>
        <p style="margin:0; color: lightgrey; padding-left: 0.5rem;">{{ reviewDetail.comment_set.length}}</p>
      </div>
      <comment></comment>
    </div>
  </div>
</template>

<script>
import StarRating from 'vue-star-rating'
import Comment from '@/components/review/comment/Comment'

import axios from 'axios'
import { mapState, mapActions } from 'vuex'


export default {
  name: 'ReviewDetail',
  components: {
    Comment,
    StarRating,
  },
  data: function () {
    return {
      starRating: null,
    }
  },
  methods: {
    updateReview: function () {
      this.$router.push({ name: 'ReviewUpdate', 
      params: {
        reviewId: this.reviewDetail.id, 
        movieTitle: this.reviewDetail.movie_id.title,
        title: this.reviewDetail.title,
        content: this.reviewDetail.content,
        rank: this.reviewDetail.rank,
        movieId: this.reviewDetail.movie_id.id
        }
      })
    },
    deleteReview: function () {
      if (confirm("정말 삭제하시겠습니까??") == true){    //확인
        axios({
          method: 'delete',
          url: `${this.tmpUrl}/community/movie/${this.reviewDetail.movie_id.id}/review/${this.reviewDetail.id}`,
          headers: this.header
        })
        .then(() => {
          this.$store.dispatch('deleteReviewDetail')
          this.$router.push({ name: 'Review' })
        })
        .catch(err => {
          console.log(err)
        })
        }else{   //취소
          return;
      }
    },
    reviewLike: function () {
      axios({
        method: 'post',
        url: `${this.tmpUrl}/community/review/${this.reviewDetail.id}/like/`,
        headers: this.header
      })
      .then(() => {
        this.$store.dispatch('getReviewDetail', this.$route.params.review_pk)
      })
      .catch(err => {
        console.log(err)
      })
    },
  },
  filters: {
    filterDate: function (data) {
      return data.substring(0, 10)
    },
    filterTime: function (data) {
      return data.substring(11, 16)
    }
  },
  created: function () {
    this.$store.dispatch('getReviewDetail', this.$route.params.review_pk)
  },
  beforeDestroy: function () {
    this.$store.dispatch('deleteReviewDetail')
  },
  computed: {
    ...mapState([
      'tmpUrl',
      'header',
      'reviewDetail',
      'loginUser'
    ]),
    ...mapActions([
      'getReviewDetail'
    ]),
    likeClickedOrNot: function () {
      const isLiked = this.reviewDetail.like_users.some(user => {
        return user.username = this.loginUser
      }) 
      return isLiked
    }
  }
}
</script>

<style scoped>
  div div {
    font-family: 'Pretendard-Regular';
    color: white;
  }
  .review-box {
    border-radius: 1rem;
    width: 40rem;
    margin: 4em auto;
    background-color: #bed8f548;;
    /* background: linear-gradient(to bottom right, rgba(165, 164, 221, 0.747), #b1af44); */
    text-align: left;
  }
  .devine-box {
    background-color: #2a6b80c0;
    padding-left: 0.5rem;
    height: 3rem;
    vertical-align: middle;
  }
  .position-center {
    margin: 0;
    position: absolute;
    top: 0.8rem;
    color: rgb(255, 255, 255);
  }
  .review-date {
    padding-left: 2rem; 
    color: lightgrey; 
    font-size: 12px;
  }
  .review-content {
    height: 10rem;
    margin: 0 2em 0 0;
  }
  .test {
    color: #81e7a3;
  }
  .is-liked {
    margin-left: 2rem;
    background-color:#81e7a3;
    color: white;
  }
  .is-not-liked {
    margin-left: 2rem;
    background-color: #ffffff;
    color: #81e7a3;
  }
  .i-true {
    color: #ffffff
  }
  .i-false {
    color: #81e7a3
  }
</style>