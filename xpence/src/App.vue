<template>
  <v-app>
    <v-app-bar app color="light lighten-4" dense clipped-left>
      <v-img alt="Expence Logo"
             class="mx-2"
             max-height="80"
             max-width="80"
             contain
             :src="require('@/assets/xpence.png')"></v-img>
      <v-spacer></v-spacer>

      <div id="nav">
        <router-link to="/login">Login</router-link>
        |
        <router-link to="/register">Register</router-link>

      </div>

      <v-badge bordered bottom color="green" dot offset-x="10" offset-y="10">
        <v-avatar size="40">
          <v-img src="https://cdn.vuetifyjs.com/images/lists/2.jpg"></v-img>
        </v-avatar>
      </v-badge>
      <span class="ml-2">{{ user_data['name'] }}</span>
      <span>
           <v-btn
               icon
               color="grey">
              <v-icon>fas fa-sort-down</v-icon>
            </v-btn>
      </span>
    </v-app-bar>

    <v-card
        color="grey lighten-4"
        flat
        height="80px"
        tile
        class="mt-12">
      <v-toolbar dense height="70px">
        <v-spacer></v-spacer>
        <v-btn icon>
          <v-icon>mdi-magnify</v-icon>
        </v-btn>

        <v-btn icon>
          <v-icon>mdi-calendar</v-icon>
        </v-btn>

        <v-btn icon>
          <v-icon>mdi-filter</v-icon>
        </v-btn>
      </v-toolbar>
    </v-card>


    <v-navigation-drawer v-model="drawer" permanent color="#F4F5F9" app clipped>
      <v-list-item class="px-2 py-5">
        <v-list-item-title class="text-capitalize" align="center">
          <b>ALL MY ACCOUNTS</b>
          <account-popup></account-popup>
        </v-list-item-title>
      </v-list-item>

      <v-list nav dense>
        <v-list-item-group v-model="selectedItem" color="deep-purple">
          <v-list-item>
            <v-list-item-content>
              <router-link to="/">
                <v-list-item-title>All Accounts</v-list-item-title>
              </router-link>
            </v-list-item-content>
          </v-list-item>
          <v-list-item v-for="account in accounts" :key="account.id">
            <v-list-item-content>
              <router-link :to="`/account/${ account.id }`">
                <v-list-item-title v-text="account.name"></v-list-item-title>
              </router-link>
            </v-list-item-content>
          </v-list-item>
        </v-list-item-group>
      </v-list>
      <v-divider class="mt-6 mb-6"></v-divider>

      <!-- Lower Nav Part -->
      <profile-popup></profile-popup>


    </v-navigation-drawer>
    <v-main>
      <router-view></router-view>
    </v-main>
  </v-app>
</template>

<script>

import axios from "axios";
import AccountPopup from "@/components/AccountPopup";
import ProfilePopup from "@/components/ProfilePopup";

export default {
  name: 'App',

  components: {
    AccountPopup,
    ProfilePopup,
  },

  beforeCreate() {
    this.$store.commit("initializeStore")
    const access = this.$store.state.access

    if (access) {
      axios.defaults.headers.common['Authorization'] = "JWT " + access
    } else {
      axios.defaults.headers.common['Authorization'] = ''
    }
  },

  data: () => ({
    selectedItem: 0,
    drawer: null,
    items: [
      {icon: 'fas fa-home', text: 'Dashboard', route: '/'},
      {icon: 'fas fa-money-check-alt', text: 'Buy / Sell', route: '/hobuysme'},
      {icon: 'fas fa-dolly', text: 'Transactions', route: '/transactions'},
      {icon: 'fas fa-exchange-alt', text: 'Exchange', route: '/exchanges'},
      {icon: 'fas fa-cog', text: 'Tools', route: '/tools'},
    ],

    accounts: null,
    name: '',
    date_created: '',
    user_data: [],

    test: [1, 2, 4],
    dialog: false,

  }),


  mounted() {
    setInterval(() => {
      this.getAccess()
    }, 55000)

    // Check current now and then
    axios.get("/auth/users/me")
        .then(response => {
          console.log('CurrentUser Data.', response)
          this.user_data = response.data
          this.getAccountsByUser(this.user_data['id'])
        })
        .catch(error => {
          console.log("Something went wrong. Couldn't get user. ", error)
          this.$router.push('/login')
        })
  },

  methods: {
    // created() {
    //   getAPI.get('/accounts/', {headers: {Authorization: `Bearer ${this.$store.state.accessToken}`}})
    //       .then(response => {
    //         console.log('Great!', response.data)
    //         this.$store.state.APIData = response.data
    //       })
    //       .catch(err => {
    //         console.log('Something went wrong!', err)
    //       })
    // },
    getAccountsByUser(userId) {
      axios.get(`/api/account/by/${userId}/`)
          .then((response) => {
            console.log('Accounts by a user: ' + userId, response.data)
            this.accounts = response.data
          })
          .catch(err => {
            console.log("Unable to get Accounts by user: ", err)
          })
    },

    getAccess() {
      const accessData = {
        refresh: this.$store.state.refresh
      }
      axios.post('/auth/jwt/refresh/', accessData)
          .then(response => {
            const access = response.data.access

            console.log('Access Token: ', access)
            localStorage.setItem("access", access)
            this.$store.commit('setAccess', access)
          })
          .catch(error => {
            console.log('Something went terribly wrong: ', error)
          })
    },

  },
};
</script>

<style scoped>
#nav {
  padding: 32px;
}

a {
  font-weight: bold;
  color: #0a53be;
  text-decoration: none;
}

.router-link-exact-active {
  color: #0dcaf0;
}


</style>
