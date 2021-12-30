<template>
  <div>
    <div class="container text-dark">
      <div class="row justify-content-md-center">
        <div class="col-md-5 p-3 login justify-content-md-center">
          <h1 class="h3 mb-3 font-weight-normal text-center">Please Sign In</h1>

          <p v-if="incorrectAuth" class="red--text lighten-1">Wrong email and/or password</p>
          <form v-on:submit.prevent="submitForm" id="login-form">
            <div class="form-group">
              <input type="text" name="email" id="user" v-model="email" class="form-control" placeholder="Username">
            </div>
            <div class="form-group">
              <input type="password" name="password" id="pass" v-model="password" class="form-control"
                     placeholder="Password">
            </div>
            <button type="submit" class="btn btn-lg btn-primary btn-block">Login</button>
          </form>

        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: 'Login',
  data() {
    return {
      email: '',
      password: '',
      incorrectAuth: false
    }
  },
  methods: {
    submitForm() {
      axios.defaults.headers.common['Authorization'] = ''
      localStorage.removeItem('access')

      const formData = {
        email: this.email,
        password: this.password
      }

      axios.post('auth/jwt/create/', formData)
      .then(response => {
        console.log('Successfully logged in: ', response)
        const access = response.data.access
        const refresh = response.data.refresh

        this.$store.commit('setAccess', access)
        this.$store.commit('setRefresh', refresh)

        axios.defaults.headers.common['Authorization'] = "JWT " + access

        localStorage.setItem("access", access)
        localStorage.setItem("refresh", refresh)

        this.$router.push("/")

      })
      .catch(error => {
        console.log('Something went terribly wrong.', error)
      })
    }
  }
}
</script>

<style>
body {
  background-color: #f4f4f4;
}

#login-form {
  padding: 32px;
}

.form-group {
  margin: 8px;
}
</style>