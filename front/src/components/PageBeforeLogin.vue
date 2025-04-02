<script setup>
import { useRouter } from 'vue-router'
import axios from 'axios'; // Importa Axios
import { endpoints } from '/common/endpoints'; // Importa gli endpoint da dove li hai definiti

const router = useRouter();

const getCsrfToken = () => {
  let cookies = document.cookie.split('; ');
  for (let cookie of cookies) {
    let [name, value] = cookie.split('=');
    if (name === 'csrftoken') return value;
  }
  return '';
};

const logout = () => {
  axios.post(`${endpoints.logout}`, {}, {
    withCredentials: true,
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": getCsrfToken(),
    },
  })
  .then(response => {
    // Pulisce il localStorage e sessionStorage
    localStorage.removeItem('auth_token');
    sessionStorage.removeItem('auth_token');
    
    // Reindirizza alla pagina di login
    router.push('/login');
  })
  .catch(error => {
    console.error('Errore nel logout:', error);
    alert('Errore nel logout: ' + (error.response?.data?.message || 'Errore sconosciuto'));
    
    // Reindirizza alla pagina di login in caso di errore
    router.push('/login');
  });
};

</script>

<template>
  <div class="container">
    <div class="content">
      <h1>Hello User</h1>
      <button @click="logout">Logout</button>
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
