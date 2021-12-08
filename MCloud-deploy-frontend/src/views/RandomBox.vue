<template>
  <div class="random-box-container">
    <random-box-cube class="box-position"></random-box-cube>
  </div>
</template>

<script>
import RandomBoxCube from '@/components/randombox/RandomBoxCube'


export default {
  name: 'RandomBox',
  components: {
    RandomBoxCube,
  }
}
</script>

<style>
  .random-box-container {
    height: 100vh;
    position: relative;
  }
  .box-position {
    margin-top: 32vh;
  }
</style>