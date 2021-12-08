import Vue from 'vue'
import VueRouter from 'vue-router'

// 낱개
import Main from '@/views/Main'
import Entrance from '@/views/Entrance'
import Profile from '@/views/Profile'
import Recommand from '@/views/Recommand'
import RandomBox from '@/views/RandomBox'
// movie
import Movie from '@/views/movie/Movie'
import MovieDetail from '@/views/movie/MovieDetail'
// review
import Review from '@/views/review/Review'
import ReviewDetail from '@/views/review/ReviewDetail'
import ReviewCreate from '@/views/review/ReviewCreate'
import ReviewUpdate from '@/views/review/ReviewUpdate'

Vue.use(VueRouter)

const routes = [
  // 
  {
    path: '/entrance',
    name: 'Entrance',
    component: Entrance
  },
  {
    path:'/',
    name: 'Main',
    component: Main,
  },

  // profile
  {
    path: '/profile/:username',
    name: 'Profile',
    component: Profile
  },
  
  // recommand
  {
    path: '/recommand',
    name: 'Recommand',
    component: Recommand
  },

  {
    path: '/randombox',
    name: 'RandomBox',
    component: RandomBox
  },

  // movie
  {
    path: '/movie',
    name: 'Movie',
    component: Movie
  },
  {
    path: '/movie/:movie_pk',
    name: 'MovieDetail',
    component: MovieDetail
  },

  // review
  {
    path: '/review',
    name: 'Review',
    component: Review
  },
  {
    path: '/movie/review/create',
    name: 'ReviewCreate',
    component: ReviewCreate
  },
  {
    path: '/movie/review/:review_pk',
    name: 'ReviewDetail',
    component: ReviewDetail
  },
  {
    path: '/movie/review/:review_pk/update',
    name: 'ReviewUpdate',
    component: ReviewUpdate
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
