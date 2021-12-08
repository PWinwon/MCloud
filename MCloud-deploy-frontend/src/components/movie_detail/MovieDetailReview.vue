<template>
  <div class="parent-box">
    <div class="review-item-box">
      <div class="left-son">
        <star-rating 
          v-if="review"
          :increment="0.5" 
          :inline="true" :star-size="20" 
          :read-only="true" :show-rating="false" 
          :rating="review.rank / 2"
          :inactive-color="'#ffffff'"
          style="padding-right: 2rem;"
        ></star-rating>   
        <div style="display: flex; align-items:flex-end">
          <p style="flex:1; margin: 0; font-weight: bold;">{{ review.user_id.username }}</p>
          <p style="flex:1; margin: 0; color: lightgrey;">{{ review.created_at.substring(0,10) }}</p>
        </div>             
      </div>
      <div class="center-son">
        {{review.title}}
      </div>
      <div class="center-2-son">
        <p style="cursor: pointer;" @click="goReviewDetail">더보기</p>
      </div>
      <div class="right-son">
        <div class="like-box">
          <i class="far fa-thumbs-up fa-lg" style="color: blue; padding: auto 0;"></i>
          <p style="color: blue;">{{ review.review_like_count }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import StarRating from 'vue-star-rating'

export default {
  name: 'MovieDetailReview',
  components: {
    StarRating
  },
  props: {
    review: Object
  },
  methods: {
    goReviewDetail: function () {
      this.$router.push({ name: 'ReviewDetail', params: { review_pk: this.review.id }})
    }
  }
}
</script>

<style scoped>
  .parent-box {
    width: 100%;
    height: 6rem;
    text-align: left;
    display: flex;
    border: 2px solid white;
    border-radius: 0 0 2rem;
    margin: 0.5rem 0;
  }

  .review-item-box {
    text-align: left;
    display: flex;
    height: 100%;
    padding: 1rem;
  }

  .left-son {
    flex: 3.5; 
    display: flex; 
    flex-direction: column; 
    justify-content: space-around;
  }

  .center-son {
    align-self: center; 
    flex: 7;
  }
  .center-2-son {
    flex: 1;
    align-self: center;
    text-decoration: underline;
  }
  .right-son {
    flex:1.5;
    align-self: center;
    height: 75%;
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .like-box {
    width: 50%;
    height: 60%;
    background-color: white;
    border-radius: 0.5rem;
    vertical-align: middle;
    display: flex;
    align-items: center;
    justify-content: space-around;
  }
</style>