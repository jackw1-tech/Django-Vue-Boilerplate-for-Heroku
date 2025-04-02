<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

const goToAnotherPage = () => {
  router.push('/login')
}
</script>

<template>
  <div class="container">
    <div class="content">
      <h1>Hello</h1>
      <h4>This is a Django/Vue/Heroku/Supabase</h4>
      <h5>Boilerplate</h5>
      <button @click="goToAnotherPage">Next Page</button>
    </div>
  </div>
</template>

<style scoped>
.container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  text-align: center;
}

.content {
  display: flex;
  flex-direction: column;
  align-items: center;
}

button {
  background-color: #42b983;
  color: white;
  border: none;
  padding: 10px 15px;
  cursor: pointer;
  border-radius: 5px;
  font-size: 16px;
  margin-top: 10px;
}

button:hover {
  background-color: #369f75;
}
</style>
