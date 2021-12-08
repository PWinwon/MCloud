<template lang="html">
  <div class=container>
    <div class="center con-switch container btn-batch">
      <div class="switch-btn">
        <vs-switch :val="12" color="#707999" v-model="options" @click="updateFilter">
          모험
        </vs-switch>
      </div>
      <div class="switch-btn">
        <vs-switch :val="14" color="#707999" v-model="options" @click="updateFilter">
          판타지
        </vs-switch>
      </div>
      <div class="switch-btn">
        <vs-switch :val="16" color="#707999" v-model="options" @click="updateFilter">
          애니메이션
        </vs-switch>
      </div>
      <div class="switch-btn">
        <vs-switch :val="18" color="#707999" warn v-model="options" @click="updateFilter">
          드라마
        </vs-switch>
      </div>
      <div class="switch-btn">
        <vs-switch :val="27" color="#707999" v-model="options" @click="updateFilter">
          공포
        </vs-switch>
      </div>
      <div class="switch-btn">
        <vs-switch :val="28" color="#707999" v-model="options" @click="updateFilter">
          액션
        </vs-switch>
      </div>
      <div class="switch-btn">
        <vs-switch :val="35" color="#707999" v-model="options" @click="updateFilter">
          코미디
        </vs-switch>
      </div>
      <div class="switch-btn">
        <vs-switch :val="36" color="#707999" v-model="options" @click="updateFilter">
          역사
        </vs-switch>
      </div>
      <div class="switch-btn">
        <vs-switch :val="37" color="#707999" v-model="options" @click="updateFilter">
          서부
        </vs-switch>
      </div>
      <div class="switch-btn">
        <vs-switch :val="53" color="#707999" v-model="options" @click="updateFilter">
          스릴러
        </vs-switch>
      </div>
      <div class="switch-btn">
        <vs-switch :val="80" color="#707999" v-model="options" @click="updateFilter">
          범죄
        </vs-switch>
      </div>
      <div class="switch-btn">
        <vs-switch :val="99" color="#707999" v-model="options" @click="updateFilter">
          다큐멘터리
        </vs-switch>
      </div>
      <div class="switch-btn">
        <vs-switch :val="878" color="#707999" v-model="options" @click="updateFilter">
          SF
        </vs-switch>
      </div>
      <div class="switch-btn">
        <vs-switch :val="9648" color="#707999" v-model="options" @click="updateFilter">
          미스터리
        </vs-switch>
      </div>
      <div class="switch-btn">
        <vs-switch :val="10402" color="#707999" v-model="options" @click="updateFilter">
          음악
        </vs-switch>
      </div>
      <div class="switch-btn">
        <vs-switch :val="10749" color="#707999" v-model="options" @click="updateFilter">
          로맨스
        </vs-switch>
      </div>
      <div class="switch-btn">
        <vs-switch :val="10751" color="#707999" v-model="options" @click="updateFilter">
          가족
        </vs-switch>
      </div>
      <div class="switch-btn">
        <vs-switch :val="10752" color="#707999" v-model="options" @click="updateFilter">
          전쟁
        </vs-switch>
      </div>
      <div class="switch-btn">
        <vs-switch :val="10770" color="#707999" v-model="options" @click="updateFilter">
          TV 영화
        </vs-switch>
      </div>
    </div>
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
  name: 'MovieFilter',
  data: function () {
    return {
      options: [],
    }
  },
  methods: {
    updateFilter: function () {
      this.$store.dispatch('getOptions', this.options)
    },
  },
  created: function () {
    this.updateFilter()
  }
}
</script>

<style>
.switch-btn {
  padding: 0.5rem;
}

.btn-batch {
  width: 90%;
}


</style>