<template>
  <div>
    <div class="comment-grid" style="padding: 0 2rem;">
      <p style="font-weight: bold;">{{ comment.user_id.username }}</p>
      <div v-if="loginUser===comment.user_id.username">
        <div class="comment-update-or-not" v-if="isClicked === false">
          <div style="padding: 1rem;">{{ comment.content}}</div>
          <span class="container" style="align-items: center;">
            <button @click="changeClicked" class="comment-btn">수정</button>
            <button @click="deleteComment" class="comment-btn">삭제</button>
          </span>
        </div>
        <div class="comment-update-or-not" style="align-items: center;" v-else>
          <div class="container" style="flex-direction: column">
            <textarea name="" id="" cols="10" rows="10" v-model="comment.content"></textarea>
          </div>
          <div class="container">
            <button class="comment-btn" @click="updateComment">완료</button>
          </div>
        </div>
      </div>
      <div v-else>

      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { mapState} from 'vuex'

export default {
  name: 'CommentListItem',
  props: {
    comment: Object
  },
  data: function () {
    return {
      isClicked: false,
    }
  },
  methods: {
    changeClicked: function () {
      this.isClicked = !this.isClicked
    },
    updateComment: function () {
      axios({
        method: 'put',
        url: `${this.tmpUrl}/community/review/comment/${this.comment.id}/`,
        data: {
          content: this.comment.content
        },
        headers: this.header
      })
      .then(() => {
        this.$store.dispatch('getReviewDetail', this.comment.review_id)
        this.isClicked = false
      })
    },
    deleteComment: function () {
      if (confirm("정말 삭제하시겠습니까??") == true){
        axios({
          method: 'delete',
          url: `${this.tmpUrl}/community/review/comment/${this.comment.id}/`,
          headers: this.header
        })
        .then(() => {
          this.$store.dispatch('getReviewDetail', this.comment.review_id)
        })
        .catch(err => {
          console.log(err)
        })
      } else {
        return
      }
    }
    
  },
  computed: {
    ...mapState([
      'tmpUrl',
      'header',
      'loginUser'
    ])
  },
  beforeDestroy: function () {
    this.isClicked = false
  },
}
</script>

<style scoped>
 button {
   font-family: 'Pretendard-Regular';
 }
 .comment-btn {
   border: none;
   border-radius: 0.5rem;
   margin: 0 2px;
   font-size: 12px;
 }
 .comment-grid {
  display:grid;
  grid-template-columns: 1fr 11fr; 
  grid-template-rows: 1fr;
 }
 .comment-update-or-not {
   display: grid;
   grid-template-columns: 5fr 1fr;
   height: 100%;
 }
  textarea {
   height: 2rem;
   border: none;
   border-radius: 0.5rem;
   background-color: white;
   font-family: 'Pretendard-Regular';
   white-space:inherit;
   word-break:normal;
   text-overflow:clip;
 }
</style>