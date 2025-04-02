<script setup>
import { ref } from 'vue'
import { endpoints } from '/common/endpoints';
import { useRouter } from 'vue-router'

const router = useRouter()

const username = ref('')
const password = ref('')
const loading = ref(false)

const goToAnotherPage = () => {
  router.push('/registration')
}

const getCsrfToken = () => {
  let cookies = document.cookie.split('; ');
  for (let cookie of cookies) {
    let [name, value] = cookie.split('=');
    if (name === 'csrftoken') return value;
  }
  return '';
}

const login = async () => {
  loading.value = true;
  const response = await fetch(`${endpoints.login}`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded',
      'X-CSRFToken': getCsrfToken()
    },
    body: new URLSearchParams({
      'username': username.value,
      'password': password.value,
    }),
    credentials: 'include'
  });

  const data = await response.json();
  if (response.ok) {
    console.log('Login riuscito:', data.message);
    router.push('/dashboard');
  } else {
    console.error('Errore di login:', data.error);
  }
  loading.value = false;
}
</script>

<template>
  <div class="container">
    <div class="login-box">
      <h2>Login</h2>
      <form @submit.prevent="login">
        <input type="text" v-model="username" placeholder="Username" required />
        <input type="password" v-model="password" placeholder="Password" required />
        <button type="submit" :disabled="loading">{{ loading ? 'Logging in...' : 'Login' }}</button>
      </form>
      <button class="secondary" @click="goToAnotherPage">Sign Up</button>
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
  background-color: #f4f4f4;
}

.login-box {
  max-width: 320px;
  padding: 20px;
  background: white;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

input {
  display: block;
  width: 100%;
  margin: 10px 0;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

button {
  width: 100%;
  background-color: #42b983;
  color: white;
  border: none;
  padding: 10px;
  cursor: pointer;
  border-radius: 5px;
  font-size: 16px;
}

button:hover {
  background-color: #369f75;
}

button.secondary {
  background-color: #ddd;
  color: #333;
}
</style>
