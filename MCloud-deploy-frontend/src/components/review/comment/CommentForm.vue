<template>
  <div class="comment-form">
    <div class="text-box">
      <textarea 
        cols="67" 
        rows="2" 
        placeholder="댓글 입력" 
        v-model="content"
        @keyup.enter="setComment"
      ></textarea>
    </div>
    <div style="flex: 1;">
      <vs-button
        color="#98bcff"
        @click="setComment"
        class="submit-btn"
      >
        작성
      </vs-button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { mapState } from 'vuex'

export default {
  name: 'CommentForm',
  data: function () {
    return {
      content: ''
    }
  },
  methods: {
    setComment: function () {
      if (this.content != '') {
        console.log(this.content)
        this.isContentNull = false
        axios({
          method: 'post',
          url: `${this.tmpUrl}/community/review/${this.reviewDetail.id}/comment/`,
          data: {
            content: this.content
          },
          headers: this.header
        })
        .then((res) => {
          this.content = null
          console.log(res.data)
          // this.$store.dispatch('setComment',res.data)
          this.$store.dispatch('getReviewDetail', this.reviewDetail.id)
        })
        .catch(err => {
          console.log(err)
        })
      } else {
        this.isContentNull = true
      }

    },
    changeNull: function () {
      this.isContentNull = false
    }
  },
  computed: {
    ...mapState([
      'tmpUrl',
      'reviewDetail',
      'header'
    ])
  }

}
</script>

<style scoped>

 .comment-form {
   display: flex;
   justify-content: space-around;
   height: 3rem;
   align-items: center;
 }
  .submit-err {
    font-size: 0.75em;
    right: 50%;
    position: absolute;
    color: red;
  }
  textarea {
    height: 2rem;
    border: none;
    border-radius: 0.5rem;
    background-color: white;
    font-family: 'Pretendard-Regular';
    margin: 0.5rem 1rem 0;
  }
  .submit-btn {
    border: none;
    border-radius: 0.5rem;
    font-size: 1rem;
    color: white
}

  .text-box {
    flex: 6.5;
    text-align: center;
  }

  .test {
    color: #98bcff;
  }
</style>