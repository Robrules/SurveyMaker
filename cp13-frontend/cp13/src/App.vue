<script>
import TheNavBar from './components/TheNavBar';
import TheFooter from './components/TheFooter';

export default {
  components: {
    TheFooter,
    TheNavBar,
  }
}

</script>

<template>
  <div id="app">
    <TheNavBar></TheNavBar>
    <div id="router-wrapper"><router-view/></div>
    <the-footer v-if="$route.name !== 'Survey Builder'" />
  </div>
</template>

<style scoped>
  #app {
    font-family: sans-serif;
    display: flex;
    height: 100vh;
    max-height: 100vh;
    flex-direction: column;
  }

  #router-wrapper {
    flex: 2;
  }
</style>
<style>
h1, h2 {
  font-weight: 300;
}
</style>
