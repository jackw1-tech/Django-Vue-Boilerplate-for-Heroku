<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'
import { endpoints } from '/common/endpoints';

const email = ref('')
const utente = ref('')
const password = ref('')
const confirmPassword = ref('')
const router = useRouter()

const register = async () => {
  if (password.value !== confirmPassword.value) {
    alert('Passwords do not match!')
    return
  }

  const data = {
    email: email.value,
    password: password.value,
    username: utente.value,
  }

  try {
 
    const response = await axios.post(`${endpoints.register}`, data)

    if (response.status === 201) {
      alert('Registration successful!')
      router.push('/login')
    }
  } catch (error) {
    console.error('Registration error:', error)
    alert('Errore durante la registrazione, riprova più tardi.')
  }
}

const goToLogin = () => {
  router.push('/login')
}
</script>


<template>
  <div class="container">
    <div class="register-box">
      <h2>Register</h2>
      <form @submit.prevent="register">
        <input type="user" v-model="utente" placeholder="User" required />
        <input type="email" v-model="email" placeholder="Email" required />
        <input type="password" v-model="password" placeholder="Password" required />
        <input type="password" v-model="confirmPassword" placeholder="Confirm Password" required />
        <button type="submit">Register</button>
      </form>
      <button class="secondary" @click="goToLogin">Sign In</button>
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

.register-box {
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
  margin-top: 10px;
}

button.secondary {
  background-color: #ddd;
  color: #333;
}

button:hover {
  background-color: #369f75;
}

button.secondary:hover {
  background-color: #bbb;
}
</style>
