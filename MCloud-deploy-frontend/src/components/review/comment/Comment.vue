<template>
  <div>
    <comment-form></comment-form>
    <comment-list></comment-list>
  </div>
</template>

<script>
import CommentForm from '@/components/review/comment/CommentForm'
import CommentList from '@/components/review/comment/CommentList'

export default {
  name: 'Comment',
  components: {
    CommentForm,
    CommentList
  },
}
</script>

<style>

</style>