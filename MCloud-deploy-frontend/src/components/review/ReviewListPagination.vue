<template>
  <div class="center">
    <vs-pagination circle v-model="page" :length="maxPage" color="#707999" @input="movePage"/>
  </div>
</template>

<script>
import Vue from 'vue'
import Vuesax from 'vuesax'
import 'vuesax/dist/vuesax.css'

Vue.use(Vuesax, {
  colors: {
    primary:'#5b3cc4',
    success:'rgb(23, 201, 100)',
    danger:'rgb(242, 19, 93)',
    warning:'rgb(255, 130, 0)',
    dark:'rgb(36, 33, 69)',
    mypink: '#ffbdbd'
  }
})

export default {
  name: 'ReviewListPagination',
  data:() => ({
    page: 1
  }),
  props: {
    maxPage: Number,
  },
  methods: {
    movePage: function () {
      this.$emit('page-data', this.page)
    }
  }
}
</script>

<style>

</style>