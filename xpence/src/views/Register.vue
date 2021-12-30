<template>
  <div>
    <div class="container text-dark">
      <div class="row justify-content-md-center">
        <div class="col-md-5 p-3 login justify-content-md-center">
          <h1 class="h3 mb-3 font-weight-normal text-center">Please Sign Up</h1>

          <form id="sign-up" @submit.prevent="submitForm">
            <div class="form-group">
              <input type="text" name="name" id="name" v-model="name" class="form-control" placeholder="Username">
            </div>
            <div class="form-group">
              <input type="text" name="email" id="user" v-model="email" class="form-control" placeholder="Email" required>
            </div>
            <div class="form-group">
              <input type="text" name="phone" id="phone" v-model="phone" class="form-control"
                     placeholder="Phone Number">
            </div>
            <div class="form-group">
              <input type="password" name="password" id="pass" v-model="password" class="form-control"
                     placeholder="Password" required>
            </div>
            <button type="submit" class="btn btn-lg btn-primary btn-block">Register</button>
          </form>

        </div>
      </div>
    </div>
  </div>
</template>

<script>

import axios from "axios";

export default {
  name: "Register",
  data() {
    return {
      phone: "",
      name: "",
      email: "",
      password: "",
      password_confirmation: "",
      // is_admin: null
    }
  },
  methods: {
    submitForm() {
      const formData = {
        email: this.email,
        phone: this.phone,
        name: this.name,
        password: this.password,
      }
      axios.post('/auth/users/', formData)
      .then(response => {
        console.log(response)
        this.$router.push('/login')
      }).catch(error => {
        console.log('There is something wrong here: ', error)
      })
    }
  }
}
</script>

<style scoped>
#sign-up {
  padding: 32px;
}

.form-group {
  margin: 8px;
}
</style>