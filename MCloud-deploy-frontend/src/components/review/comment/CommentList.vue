<template>
  <div>
    <div v-if="reviewDetail.comment_set.length != 0">
      <comment-list-item
        v-for="comment in reviewDetail.comment_set.slice().reverse()"
        :key="comment.id"
        :comment="comment"
      ></comment-list-item>
    </div>
    <div v-else>
      <div class="container" style="height: 3rem; align-items: center">댓글을 작성해주세요.</div>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex'

import CommentListItem from '@/components/review/comment/CommentListItem'

export default {
  name: 'CommentList',
  components: {
    CommentListItem
  },
  props: {
    review: Object,
  },
  computed: {
    ...mapState([
      'tmpUrl',
      'reviewDetail'
    ]),
  },
}
</script>

<style>

</style>