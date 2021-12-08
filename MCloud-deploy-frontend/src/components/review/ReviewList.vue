<template>
  <div style="width: 72rem; margin: 0 auto;">
    <div class="parent-box">
      <div class="son-id">id</div>
      <div class="son-movie-title">영화</div>
      <div class="son-title">제목</div>
      <div class="son-rank">평점</div>
      <div class="son-recommend">추천</div>
      <div class="son-date">날짜</div>
    </div>
    <review-list-item 
      v-for="(review, idx) in pageReviews"
      :key=idx
      :review="review"
    ></review-list-item>
    <review-list-pagination
      @page-data="getPageData"
      :max-page="getMaxPage"
    ></review-list-pagination>
  </div>
</template>

<script>
import ReviewListPagination from '@/components/review/ReviewListPagination'
import ReviewListItem from '@/components/review/ReviewListItem'
import { mapState } from 'vuex'

export default {
  name: 'ReviewList',
  components: {
    ReviewListItem,
    ReviewListPagination
  },
  data: function () {
    return {
      pageCnt: 1,
    }
  },
  computed: {
    ...mapState([
      'reviews'
    ]),
    pageReviews: function () {
      let pageReviewList = []
      let start = (this.pageCnt - 1) * 10
      let end = start + 10
      pageReviewList = this.reviews.slice().reverse().filter((review, index) => {
        return (index >= start && index < end)
      })
      return pageReviewList
    },
    getMaxPage: function () {
      return parseInt(this.reviews.length / 10) + 1
    }
  },
  methods: {
    getPageData: function (page) {
      this.pageCnt = page
    }
  }
}
</script>

<style scoped>
  .parent-box {
    width: 100%;
    display: flex;
    align-items: center; 
    text-align: center; 
    font-weight: bold;
    background-color: #55d5ff7c;
  }
  .son-id {
    flex: 1.25;
  }
  .son-movie-title {
    text-align: left;
    flex: 1.5;
  }
  .son-title {
    text-align: left;
    flex: 2.5;
  }
  .son-rank {
    flex: 1.25;
  }
  .son-recommend{
    flex: 1.25;
  }
  .son-date {
    flex:1.5;
  }
</style>