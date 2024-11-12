<template>
  <div id="app">
    <SssGameList />
  </div>
</template>

<script>
import SssGameList from './components/SssGameList.vue';

export default {
  name: 'App',
  components: {
    SssGameList
  }
};
</script>

<style>

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
